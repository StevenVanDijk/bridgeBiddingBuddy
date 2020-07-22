from bidding_tree import bids
import pytest

testcases = [
    ("you open", [], 12, 3, 5, 2, 0, "1Hs", "Normal_5card"),
    ("you open pass", [], 11, 0, 0, 5, 0, "pass", "open_pass"),
    ("you open preemtif", [], 8, 7, 0, 0, 0, '3Ss', "preemtif3"),
    ("you open 1SA", [], 16, 5, 2, 3, 3, '1SA', "1SA_opening"),
    ("you open 1Cs", [], 13, 4, 4, 3, 2, '1Cs', "1Cs_opening"),
    ("you open 2SA", [], 21, 5, 2, 3, 4, '2SA', '2SA_opening'),
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
    ("preemptief3", [], 8, 0, 7, 0, 0,'3Hs', "preemtif3"),
    ("answer pass", ["1Ss", "pass"], 2, 4, 0, 0, 0, 'pass'),
    ("informatiedoublet", ['1Ss'], 13, 3, 4, 3, 3, 'X'),
    ("answer 1SA 6 card", ['1SA', 'pass', '2hs', 'pass', '2Ss', 'pass'], 11, 6, 0, 0, 0, '4Ss'),
    ("volgbod", ['1Ds'], 9, 0, 5, 0, 0, "1Hs"),
    ("preemptief volgbod", ['1Ds'], 8, 0, 7, 0, 0, "3Hs"),
    ("preemptief4", [], 3, 0, 0, 0, 8, "4Cs"),
    ("weak2", [], 8, 0, 0, 6, 0, "Ds", "2Ds"),
    ("invite3", ["pass", "1Hs", "pass"], 10, 5, 3, 2, 2, "Ss", "3Hs"),
    ("acceptinvite3", ['1Hs', 'pass', '3Hs', 'pass'], 15, 5, 0, 0, 0, '4Ss'),
    ('passto2sa', ['2sa', "pass"], 2, 0, 0, 0, 4, "pass"),
    ('roundpass', ["pass", "pass", "pass"], 11, 0, 0, 5, 0, "pass", 'rondpass')
    ]

@pytest.mark.parametrize('descr, cb, points, schoppen, harten, ruiten, klaveren, expected, explain', testcases)
def testBidding(descr, cb, points, schoppen, harten, ruiten, klaveren, expected, explain):
    def pretty(s):
        return s.replace("Hs", "♥").replace("Ss", "♠").replace("Ds", "♦").replace("Cs", "♣")
    
    current = [pretty(b) for b in cb]
    assert bids(current, points, schoppen, harten, ruiten, klaveren) == (pretty(expected), explain)

