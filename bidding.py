from typing import List
from constants import colors

def biddingIsAllowed(previousBids, bid):
    currentBid = Bidding()
    for b in previousBids:
        currentBid.addBid(b)
    return currentBid.isAllowed(bid)
    
class Bidding:
    playOrder = ["N", "E", "S", "W"]
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
        self.whoStarts = 'N'
        self.nrOfPoints = None
        self.nrOfCards = {}

    def contract(self):
        current = list(self.current)
        contract = ''
        dealer = self.whoStarts
        
        def Leader(dealer, current):
            count_bids = len(current)
            rest = count_bids % 4
            leader = ''

            if rest == 0:
                leader = dealer

            else:
                if dealer == 'O':
                    rest -= 1
                if dealer == 'Z':
                    rest -= 2
                if dealer == 'W':
                    rest -= 3

                if rest == 0:
                    leader = 'N'
                if rest == 1:
                    leader = 'O'
                if rest == 2:
                    leader = 'Z'
                if rest == 3:
                    leader = 'W'

            return leader

        leader = Leader(dealer, current)

        def remove_last_passes(current):
            count_pass = 0
            done = False
            while not done:
                if len(current) >= 1:
                    if current[-1] == 'pass':
                        current.remove('pass')
                        count_pass += 1
                    else:
                        done = True
                else: 
                    done = True
            return current


        remove_last_passes(current)
        contract = current[-1]

        return (contract, leader)