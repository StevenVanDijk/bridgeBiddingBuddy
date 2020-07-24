from bidding import Bidding

def testIsAllowed():
    bidding = Bidding()
    assert bidding.isAllowed('pass')
    
def testIsDblAllowed():
    bidding = Bidding()

    bidding.current = [ ]
    assert not bidding.isAllowed('X')

    bidding.current = [ '1♣', '2♦' ]
    assert bidding.isAllowed('X')

    bidding.current = [ '1♣', '2♦', 'pass' ]
    assert not bidding.isAllowed('X')

    bidding.current = [ '1♣', '2♦', 'X' ]
    assert not bidding.isAllowed('X')

    bidding.current = [ '1♣', '2♦', 'pass', 'pass' ]
    assert bidding.isAllowed('X')

    bidding.current = ['1♣', 'X']
    assert not bidding.isAllowed('X')


def testIsRdblAllowed():
    bidding = Bidding()

    bidding.current = ["1♣", 'X']
    assert bidding.isAllowed('XX')


def testDoubleRdbl():
    bidding = Bidding()

    bidding.current = ["1♣", 'XX']
    assert not bidding.isAllowed('XX')


def testRdblnoDbl():
    bidding = Bidding()

    bidding.current = ['1♣']
    assert not bidding.isAllowed('XX')

def testNoDblOnPartner():
    bidding = Bidding()

    bidding.current = ['X', 'X', 'pass']

    assert not bidding.isAllowed('X')
