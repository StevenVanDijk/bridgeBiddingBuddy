from bidding import Bidding
from biddingEncoder import BiddingEncoder
from constants import colors
import json


def testEncodesEmptyBidding():
    a = Bidding()
    enc = BiddingEncoder()
    obj = enc.default(a)
    assert obj == {"current": [], "whoStarts": 'N',
                   "nrOfPoints": None, "nrOfCards": {}}


def testSerializesEmptyBidding():
    a = Bidding()
    result = json.dumps(a, cls=BiddingEncoder, ensure_ascii=False)
    assert result == '{"current": [], "whoStarts": "N", "nrOfPoints": null, "nrOfCards": {}}'


def testSerializesBids():
    a = Bidding()
    a.current = ['pass', 'X', '1♣']
    result = json.dumps(a, cls=BiddingEncoder, ensure_ascii=False)
    assert result == '{"current": ["pass", "X", "1♣"], "whoStarts": "N", "nrOfPoints": null, "nrOfCards": {}}'


def testSerializeCards():
    a = Bidding()
    a.nrOfPoints = 21
    i = 3
    for color in colors:
        a.nrOfCards[color] = i
        i = i + 1

    result = json.dumps(a, cls=BiddingEncoder, ensure_ascii=False)
    assert result == '{"current": [], "whoStarts": "N", "nrOfPoints": 21, "nrOfCards": {"♣": 3, "♦": 4, "♥": 5, "♠": 6}}'
