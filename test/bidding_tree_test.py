from bidding_tree import bidding_tree
import pytest

testcases = [
    ("you open", [], 12, 3, 5, 2, 0, "1Hs"),
    ("you open pass", [], 11, 0, 0, 5, 0, "pass"),
    ("you open preemtif", [], 8, 7, 0, 0, 0, '3Ss'),
    ("you open 1SA", [], 16, 5, 2, 0, 0, '1SA'),
    ("you open 1Cs", [], 13, 4, 4, 3, 2, '1Cs'),
    ("you open 2SA", [], 21, 5, 2, 3, 4, '2SA'),
    ("you open 2Cs w pts", [], 25, 0, 0, 0, 0, '2Cs'),
    ("you open 2Cs", [], 16, 7, 0, 0, 0, '2Cs'),
    ("you open 2Hs", [], 0, 0, 6, 0, 0, '2Hs'),
    ("you open 2SA", [], 21, 5, 3, 3, 2, '2SA'),
    ("jacoby", ["1SA", "pass"], 0, 0, 5, 0, 0, '2Ds'),
    ("stayman", ["1SA", "pass"], 8, 4, 0, 0, 0, '2Cs'),
    ("answer to Stayman", ["1SA", "pass", "2♣", "pass"], 16, 0, 4, 0, 0, '2Hs'),
    ("answer 2SA to 1SA", ["1SA", "pass"], 8, 0, 0, 4, 0, '2SA'),
    ("answer 3SA to 1SA", ["1SA", "pass"], 10, 0, 0, 0, 0, '3SA'),
    ("answer to partner lvl 1", ["1Cs", "pass"], 20, 0, 4, 0, 0, '1Hs'),
    ("preemptief3", [], 8, 0, 7, 0, 0,'3Hs')]
    # ("answer pass", ["1Ss", "pass"], 2, 4, 0, 'Ss', 'pass'),
    # ("informatiedoublet", ['1Ss'], 13, 4, 3, 'Hs', 'X'),
    # ("answer 1SA 6 card", ['1SA', 'pass', '2hs', 'pass', '2Ss', 'pass'], 11, 6, 0, 'Ss', '4Ss'),
    # ("volgbod", ['1Ds'], 9, 5, 0, "Hs", "1Hs"),
    # ("preemptief volgbod", ['1Ds'], 8, 7, 0, "Hs", "3Hs"),
    # ("preemptief4", [], 3, 8, 0, "Cs", "4Cs"),
    # ("weak2", [], 8, 6, 0, "Ds", "2Ds"),
    # ("invite3", ["pass", "1Hs", "pass"], 10, 5, 2, "Ss", "3Hs"),
    # ("acceptinvite3", ['1Hs', 'pass', '3Hs', 'pass'], 15, 5, 0, 'Sch', '4sch'),
    # ('passto2sa', ['2sa', "pass"], 2, 4, 0, "Cs", "pass"),
    # ('roundpass', ["pass", "pass", "pass"], 11, 5, 0, "Ds", "pass")]









@pytest.mark.parametrize('descr, cb, points, schoppen, harten, ruiten, klaveren, expected', testcases)
def testBidding(descr, cb, points, schoppen, harten, ruiten, klaveren, expected):
    def pretty(s):
        return s.replace("Hs", "♥").replace("Ss", "♠").replace("Ds", "♦").replace("Cs", "♣")
    
    current = [pretty(b) for b in cb]
    bt = bidding_tree()
    assert bt.bids(current, points, schoppen, harten, ruiten, klaveren) == pretty(expected)

