from bidding import Bidding

class Mediator():
    bidding: Bidding = Bidding()

    def setBidding(self, bidding):
        self.bidding = bidding