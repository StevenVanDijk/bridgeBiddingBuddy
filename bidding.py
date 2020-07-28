from typing import List
from constants import colors

def biddingIsAllowed(previousBids, bid):
    currentBid = Bidding()
    for b in previousBids:
        currentBid.addBid(b)
    return currentBid.isAllowed(bid)
    
north = 'N'
east = 'E'
south = 'S'
west = 'W'
playOrder = [north, east, south, west]

class Bidding:
    biddingOrderList : List[str]

    current: list
    whoStarts: str
    nrOfPoints: int
    nrOfCards: dict

    def __init__(self):
        suitsAndSA = list(colors)
        suitsAndSA.append('SA')
        self.biddingOrderList = []
        for i in range(1, 8):
            for j in suitsAndSA:
                self.biddingOrderList.append(str(i) + j)
        self.reset()

    def getNextPlayOrder(self, currentPlay: str):
        return playOrder[(playOrder.index(currentPlay) + 1) % len(playOrder)]

    def isSpecial(self, bid):
        return bid == 'pass' or bid == 'X' or bid == 'XX'

    def setWhoStarts(self, whoStarts):
        if (len(self.current) == 0): 
            self.whoStarts = whoStarts

    def setNrOfPoints(self, value):
        self.nrOfPoints = value

    def getBidOrder(self, bid):
        return self.biddingOrderList.index(bid)

    def getLastBidOrder(self):
        previousBids = [elem for elem in self.current if not self.isSpecial(elem)]
        if len(previousBids) > 0:
            return self.getBidOrder(previousBids.pop())
        else:
            return -1

    def finished(self):
        count_biddings = len(self.current)

        if count_biddings >= 4:
            if self.current[-1] == 'pass' and self.current[-2] == 'pass' and self.current[-3] == 'pass':
                return True
        return False

    def needsSpecification(self):
        return self.nrOfPoints == None or not all([color in self.nrOfCards for color in colors])

    def isAllowed(self, bid):
        biddings_passed = len(self.current)
        if bid == 'X' and biddings_passed < 1:
            return False
        if bid == 'X':
            if self.current[-1] == 'X' or self.current[-1] == 'XX':
                return False
            if biddings_passed >= 3:
                if self.current[-2] == 'X' or self.current[-3] == 'X' and self.current[-1] == 'pass':
                    return False
        if bid == 'XX' and biddings_passed < 2:
            return False
        if bid == 'XX' and self.current[-1] != 'X':
            return False
        if not self.isSpecial(bid):
            if self.getBidOrder(bid) <= self.getLastBidOrder():
                return False        
        else:
            if bid == 'X' and biddings_passed >= 2:    
                    if self.current[-1] == 'pass' and self.current[-2] != 'pass':
                        return False
        return True
    
    def addBid(self, bid):
        if not self.isAllowed(bid):
            raise AssertionError("bid is not allowed")

        self.current.append(bid)

    def removeLastBid(self):
        if len(self.current) > 0: 
            self.current.pop()

    def reset(self):
        self.current = []
        self.whoStarts = north
        self.nrOfPoints = None
        self.nrOfCards = {}

    def getColor(self, bid):
        if len(bid) == 2 and bid[0].isdigit():
            return bid[1]
        return None

    def getLeader(self):
        leader = self.whoStarts
        currentPlayer = self.whoStarts
        firstToPlayColorNZ = {}
        firstToPlayColorOW = {}
        lastColor = None
        lastPlayer = None
        for bid in self.current:
            if (not self.isSpecial(bid)):
                lastColor = self.getColor(bid)
                lastPlayer = currentPlayer

                if currentPlayer == north or currentPlayer == south:
                    if not lastColor in firstToPlayColorNZ:
                        firstToPlayColorNZ[lastColor] = currentPlayer
                    
                if currentPlayer == east or currentPlayer == west:
                    if not lastColor in firstToPlayColorOW:
                        firstToPlayColorOW[lastColor] = currentPlayer
            currentPlayer = self.getNextPlayOrder(currentPlayer)

        if lastPlayer in [north, south]:
            return firstToPlayColorNZ[lastColor]
        
        if lastPlayer in [east, west]:
            return firstToPlayColorOW[lastColor]

        raise NotImplementedError()

    def contract(self):
        normalBids = [ bid for bid in self.current if not self.isSpecial(bid) ]
        contract = None if len(normalBids) == 0 else normalBids[-1]
        return (contract, self.getLeader())