import pytest
from bidding  import Bidding, north, south, east, west
    
def testLeaderN():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', 'pass', 'pass']
    bidding.whoStarts = 'N'

    assert bidding.contract() == ('1SA', 'Z')

def testLeaderZ():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', 'pass', 'pass']
    bidding.whoStarts = 'Z'

    assert bidding.contract() == ('1SA', 'N')
    
def testLeaderO():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', '2♦', 'pass', 'pass', 'pass']
    bidding.whoStarts = 'O'

    assert bidding.contract() == ('2♦', 'O')

def testLeaderW():
    bidding = Bidding()
    bidding.current = ['1♥', 'pass', '1SA', 'pass', '2♦', 'pass', 'pass', '2♥', 'pass', 'pass', '3♣', 'pass', 'pass', 'pass']
    bidding.whoStarts = east

    assert bidding.getLeader() == west


