from bidding_tree import bidding_tree
import pytest

testcases = [
    ("you open", [], 12, 5, 0, 'Hs', "1Hs"),
    ("you open pass", [], 11, 6, 0, 'Ss', "pass"),
    ("you open preemtif", [], 8, 7, 0, 'Ss', '3Ss'),
    ("you open 1SA", [], 16, 5, 2, 'Ss', '1SA'),
    ("you open 1Cs", [], 13, 4, 0, 'Ss', '1Cs'),
    ("you open 2SA", [], 21, 5, 2, 'Hs', '2SA'),
    ("you open 2Cs w pts", [], 25, 0, 0, 'Hs', '2Cs'),
    ("you open 2Cs", [], 16, 7, 0, 'Hs', '2Cs'),
    ("you open 2Hs", [], 0, 6, 0, 'Hs', '2Hs'),
    ("you open 2SA", [], 21, 5, 3, 'Hs', '2SA'),
    ("jacoby", ["1SA", "pass"], 0, 5, 0, 'Hs', '2Ds'),
    ("stayman", ["1SA", "pass"], 8, 4, 0, 'Hs', '2Cs'),
    ("answer to Stayman", ["1SA", "pass", "2♣", "pass"], 16, 4, 0, 'Hs', '2Hs'),
    ("answer 2SA to 1SA", ["1SA", "pass"], 8, 4, 0, 'Cs', '2SA'),
    ("answer 3SA to 1SA", ["1SA", "pass"], 10, 4, 0, 'Cs', '3SA'),
    ("answer to partner lvl 1", ["1Cs", "pass"], 90, 4, 0, 'Hs', '1Hs')
]

@pytest.mark.parametrize('descr, cb, points, highest, lowest, color, expected', testcases)
def testBidding(descr, cb, points, highest, lowest, color, expected):
    def pretty(s):
        return s.replace("Hs", "♥").replace("Ss", "♠").replace("Ds", "♦").replace("Cs", "♣")
    current = [pretty(b) for b in cb]
    bt = bidding_tree()
    assert bt.bids(current, points, highest, lowest, pretty(color)) == pretty(expected)

