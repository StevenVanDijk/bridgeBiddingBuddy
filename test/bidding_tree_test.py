from bidding_tree import bids
from typing import Tuple, List
import pytest

testcases: Tuple[str, List[str], int, int, int, int, int, str, str] = [
    ("you open", [], 12, 3, 5, 2, 0, "1Hs", "Normal_5card"),
    ("you open pass", [], 11, 0, 0, 5, 0, "pass", "open_pass"),
    ("you open preemtif", [], 8, 7, 0, 0, 0, '3Ss', "preemtif3"),
    ("you open 1SA", [], 16, 5, 2, 3, 3, '1SA', "1SA_opening"),
    ("you open 1Cs", [], 13, 4, 4, 3, 2, '1Cs', "1Cs_opening"),
    ("you open 2SA", [], 21, 5, 2, 3, 4, '2SA', '2SA_opening'),
    ("you open 2Cs w pts", [], 25, 0, 0, 0, 0, '2Cs',"2Cs_opening"),
    ("you open 2Cs", [], 16, 7, 0, 0, 0, '2Cs',"2Cs_opening"),
    ("you open 2Hs", [], 0, 0, 6, 0, 0, '2Hs',"preemtif2"),
    ("you open 2SA", [], 21, 5, 3, 3, 2, '2SA',"2SA_opening"),
    ("jacoby", ["1SA", "pass"], 0, 0, 5, 0, 0, '2Ds',"jacoby"),
    ("stayman", ["1SA", "pass"], 8, 4, 0, 0, 0, '2Cs',"stayman"),
    ("answer to Stayman", ["1SA", "pass", "2♣", "pass"], 16, 0, 4, 0, 0, '2Hs',"answer_to_stayman_colors"),
    ("answer 2SA to 1SA", ["1SA", "pass"], 8, 0, 0, 4, 0, '2SA',"1SA-2SA"),
    ("answer 3SA to 1SA", ["1SA", "pass"], 10, 0, 0, 0, 0, '3SA',"1SA-3SA"),
    ("answer to partner lvl 1", ["1Cs", "pass"], 20, 0, 4, 0, 0, '1Hs', "answering_partnerClr"),
    ("preemptief3", [], 8, 0, 7, 0, 0,'3Hs', "preemtif3"),
    ("answer pass", ["1Ss", "pass"], 2, 4, 0, 0, 0, 'pass',"normal_pass"),
    ("informatiedoublet", ['1Ss'], 13, 3, 4, 3, 3, 'X',"infoX"),
    ("answer 1SA 6 card", ['1SA', 'pass', '2Hs', 'pass', '2Ss', 'pass'], 11, 6, 0, 0, 0, '4Ss',"answeringJacoby6Crd"),
    ("volgbod", ['1Ds'], 9, 0, 5, 0, 0, "1Hs", "tussenbieden"),
    ("preemptief volgbod", ['1Ds'], 8, 0, 7, 0, 0, "3Hs", "preemtif3"),
    ("preemptief4", [], 3, 0, 0, 0, 8, "4Cs","preemtif4"),
    ("weak2", [], 8, 0, 0, 6, 0, "2Ds", "preemtif2"),
    ("invite3", ["pass", "1Hs", "pass"], 10, 5, 3, 2, 2, "3Hs","fitFoundedInviteU3"),
    ("acceptinvite3", ['1Hs', 'pass', '3Hs', 'pass'], 15, 5, 0, 0, 0, '4Ss',"answerInvite"),
    ('passto2sa', ['2sa', "pass"], 2, 0, 0, 0, 4, "pass", "normal_pass"),
    ('roundpass', ["pass", "pass", "pass"], 11, 0, 0, 5, 0, "pass", 'rondpass'),
    ('veelpunten', ['pass'], 24, 2, 4, 5, 2, '2Cs',"2Cs_opening"),
    ('matchgevonden', ['1♥', 'pass'], 15, 0, 5, 5, 3, '4Hs',"fitFoundedManchU"),
    ('matchgevonden2', ['pass', '1♥', 'pass'], 12, 4, 3, 4, 2, '4Hs',"fitFoundedManchU"),
    ('voorbereidendklaveren', ['pass'], 12, 4, 4, 3, 2, '1Cs',"1Cs_opening"),
    ('ikwilindeapptesten', ['1Hs'], 12, 5, 2, 4, 2, 'X', 'infoX'),
    ('geensaopenenmet15p', ['pass', 'pass', 'pass'], 15, 5, 5, 1, 2, '1Ss', 'Normal_5card'),
    ('tussenbod', ['pass', '1♦'], 8, 4, 5, 2, 2, '1Hs', 'tussenbieden'),
    ('ruitenisookmooi', ['pass', 'pass'], 13, 2, 4, 4, 3, '1Ds', 'Normal_4card'),
    ('fitFoundedU2Ds', ['1♦', 'pass'], 8, 2, 4, 5, 2, '1SA', 'answering_partnerSa'),
    ('2klisookeenantwoord', ['1♣', 'pass'], 8, 3, 3, 2, 5, '2Cs', 'fitFoundedU2Cs'),
    ('crash', ['1♠', 'pass'], 8, 2, 3, 4, 4, 'pass', 'unknown'),
    ('hoogstekleur', [], 15, 1, 2, 4, 6, '1Cs', 'Normal_5card')
    
    ]

@pytest.mark.parametrize('descr, cb, points, schoppen, harten, ruiten, klaveren, expected, explain', testcases)
def testBidding(descr, cb, points, schoppen, harten, ruiten, klaveren, expected, explain):
    def pretty(s):
        return s.replace("Hs", "♥").replace("Ss", "♠").replace("Ds", "♦").replace("Cs", "♣")
    
    current = [pretty(b) for b in cb]
    assert bids(current, points, schoppen, harten, ruiten, klaveren) == (pretty(expected), explain)

