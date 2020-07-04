def biddingIsAllowed(previousBids, bid):
    currentBid = Bidding()
    for b in previousBids:
        currentBid.addBid(b)
    return currentBid.isAllowed(bid)
    
class Bidding:
    playOrder = ["N", "E", "S", "W"]
    buttonsDict = {
        '1♣': 1, '2♣': 4, '3♣': 9, '4♣': 14, '5♣': 19, '6♣': 24, '7♣': 29,
        '1♦': 2, '2♦': 5, '3♦': 10, '4♦': 15, '5♦': 20, '6♦': 25, '7♦': 30,
        '1♥': 3, '2♥': 6, '3♥': 11, '4♥': 16, '5♥': 21, '6♥': 26, '7♥': 31,
        '1♠': 4, '2♠': 7, '3♠': 12, '4♠': 17, '5♠': 22, '6♠': 27, '7♠': 32,
        '1SA': 5, '2SA': 8, '3SA': 13, '4SA': 18, '5SA': 23, '6SA': 28, '7SA': 33
    }

    current = []
    whoStarts = 'N'
    bidding_ended = False
    opponent = False
    partner = False

    def isSpecial(self, bid):
        return bid == 'pass' or bid == 'X' or bid == 'XX'

    def setWhoStarts(self, whoStarts):
        if (len(self.current) == 0): 
            self.whoStarts = whoStarts

    def getLastBidOrder(self):
        previousBids = [elem for elem in self.current if not self.isSpecial(elem)]
        if len(previousBids) > 0:
            return self.buttonsDict[previousBids.pop()]
        else:
            return -1

    def finished(self):
        count_biddings = len(self.current)

        if count_biddings >= 4:
            if self.current[-1] == 'pass' and self.current[-2] == 'pass' and self.current[-3] == 'pass':
                return True
        return False

    def isAllowed(self, bid):
        biddings_passed = len(self.current)
                
        if bid == 'X' and biddings_passed < 2:
            return False
        if bid == 'X':
            if self.current[-1] == 'X':
                return False
            if biddings_passed >= 3:
                if self.current[-2] == 'X' or self.current[-3] == 'X' and self.current[-1] == 'pass':
                    return False
            
        if not self.bidding_ended:
            if not self.isSpecial(bid):
                if self.buttonsDict[bid] <= self.getLastBidOrder():
                    return False        
            else:
                if biddings_passed >= 2:    
                    if self.current[-1] == 'pass' and self.current[-2] == 'pass':
                        self.opponent = True
                        self.partner = False     
                    if self.current[-1] == 'pass':
                        if self.current[-2] != 'pass':
                            self.partner = True
                            self.opponent = False
                        else:
                            self.opponent = True
                            self.partner = False    
                if self.partner == True:
                    if bid == 'X':
                        return False
        return True
    
    def addBid(self, bid):
        if not self.isAllowed(bid):
            raise AssertionError("bid is not allowed")

        self.current.append(bid)

    def removeLastBid(self):
        self.bidding_ended = False
        if len(self.current) > 0: 
            self.current.pop()

    def reset(self):
        self.current = []