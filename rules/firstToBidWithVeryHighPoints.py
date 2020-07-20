from condition import *
from biddingRule import BiddingRule

class FirstToBidWithVeryHighPointsRule(BiddingRule):
    def __init__(self):
        super().__init__('1SA', [
            OrCondition(NoBidsMadeCondition(), LastBidEqualToCondition('pass')),
            HighestPointsBetweenCondition(20, 23),
            HighestSeriesBetweenCondition(0, 5),
            LowestSeriesBetweenCondition(2, infinite)
        ] )