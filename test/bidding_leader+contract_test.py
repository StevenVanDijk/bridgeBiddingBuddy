import pytest
from bidding  import Bidding, north, south, east, west
    
def testLeaderN():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', 'pass', 'pass']
    bidding.whoStarts = north

    assert bidding.contract() == ('1SA', south)

def testLeaderZ():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', 'pass', 'pass']
    bidding.whoStarts = south

    assert bidding.contract() == ('1SA', north)
    
def testLeaderO():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', '2♦', 'pass', 'pass', 'pass']
    bidding.whoStarts = east

    assert bidding.contract() == ('2♦', east)

def testLeaderW():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', '2♦', 'pass', 'pass', '2♥', 'pass', 'pass', '3♣', 'pass', 'pass', 'pass']
    bidding.whoStarts = east

    assert bidding.contract() == ('3♣', west)


