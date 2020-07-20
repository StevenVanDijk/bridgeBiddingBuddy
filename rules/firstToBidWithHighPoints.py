from condition import *
from biddingRule import BiddingRule

class FirstToBidWithHighPointsRule(BiddingRule):
    def __init__(self):
        super().__init__('1SA', [
            HighestPointsBetweenCondition(20, 22),
            HighestSeriesBetweenCondition(0, 5),
            LowestSeriesBetweenCondition(2, infinite)
        ])
