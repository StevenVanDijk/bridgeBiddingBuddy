from typing import List
from bidding import Bidding

infinite : int = 1000

class Condition:
    def eval(self, bidding: Bidding) -> bool:
        pass

    def explain(self) -> str:
        pass


class NoBidsMadeCondition(Condition):
    def __init__(self):
        super().__init__()

    def eval(self, bidding):
        return len(bidding.current) == 0

    def explain(self):
        return 'No bids were made'


class MaxNrPassesCondition(Condition):
    maxPasses: int

    def __init__(self, maxPasses):
        super().__init__()
        self.maxPasses = maxPasses

    def eval(self, bidding):
        return bidding.count('pass') > self.maxPasses

    def explain(self):
        return "Less passes than " + str(self.maxPasses)


class LastBidEqualToCondition(Condition):
    bid: str

    def __init__(self, bid):
        super().__init__()

        self.bid = bid

    def eval(self, bidding: Bidding):
        return len(bidding.current) > 0 and bidding.current[-1] == self.bid

    def explain(self):
        return "Last bid was " + self.bid

class HighestPointsBetweenCondition(Condition):
    min: int
    max: int

    def __init__(self, min, max):
        super().__init__()

        self.min = min
        self.max = max

    def eval(self, bidding: Bidding):
        return bidding.nrOfPoints >= self.min and bidding.nrOfPoints <= self.max

    def explain(self):
        return "Highest points between " + str(self.min) + " and " + str(self.max)

class OrCondition(Condition):
    conditions: List[Condition]

    def __init__(self, cond1, cond2):
        super().__init__()

        self.conditions = [cond1, cond2]

    def eval(self, bidding):
        return any([condition.eval(bidding) for condition in self.conditions])

    def explain(self):
        return "Either: " + str([cond.explain() for cond in self.conditions])

class HighestSeriesBetweenCondition(Condition):
    min: int
    max: int

    def __init__(self, min, max):
        super().__init__()
        self.min = min
        self.max = max

    def eval(self, bidding):
        return bidding.highestSeries >= self.min and bidding.highestSeries <= self.max

    def explain(self):
        return "Highest series between " + str(self.min) + " and " + str(self.max)

class LowestSeriesBetweenCondition(Condition):
    min: int
    max: int

    def __init__(self, min, max):
        super().__init__()
        self.min = min
        self.max = max

    def eval(self, bidding):
        return bidding.lowestSeries >= self.min and bidding.lowestSeries <= self.max

    def explain(self):
        return "Lowest series between " + str(self.min) + " and " + str(self.max)
