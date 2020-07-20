from typing import List
from bidding import Bidding
from condition import Condition

class BiddingRule:
    successfulBid: str
    conditions: List[Condition]

    def __init__(self, successfulBid, conditions):
        self.successfulBid = successfulBid
        self.conditions = conditions

    def match(self, bidding) -> bool:
        return all([cond.eval(bidding) for cond in self.conditions])

    def bidding(self) -> str:
        return self.successfulBid

    def explanation(self) -> str:
        return [cond.explain() for cond in self.conditions]


