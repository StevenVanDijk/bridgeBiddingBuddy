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
