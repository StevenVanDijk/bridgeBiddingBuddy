from bidding import Bidding
from biddingEncoder import BiddingEncoder, bid2Json, json2Bid
from constants import colors
import json


def testEncodesEmptyBidding():
    a = Bidding()
    enc = BiddingEncoder()
    obj = enc.default(a)
    assert obj == {"__type__": "Bidding", "current": [], "whoStarts": 'N', "nrOfPoints": None, "nrOfCards": {}}


def testSerializesEmptyBidding():
    a = Bidding()
    result = bid2Json(a)
    assert result == '{"__type__": "Bidding", "current": [], "whoStarts": "N", "nrOfPoints": null, "nrOfCards": {}}'


def testSerializesBids():
    a = Bidding()
    a.current = ['pass', 'X', '1♣']
    result = bid2Json(a)
    assert result == '{"__type__": "Bidding", "current": ["pass", "X", "1♣"], "whoStarts": "N", "nrOfPoints": null, "nrOfCards": {}}'


def testSerializeCards():
    a = Bidding()
    a.nrOfPoints = 21
    i = 3
    for color in colors:
        a.nrOfCards[color] = i
        i = i + 1

    result = bid2Json(a)
    assert result == '{"__type__": "Bidding", "current": [], "whoStarts": "N", "nrOfPoints": 21, "nrOfCards": {"♣": 3, "♦": 4, "♥": 5, "♠": 6}}'

def testDeserializeEmptyBidding():
    b = json2Bid('{"__type__": "Bidding", "current": [], "whoStarts": "N", "nrOfPoints": null, "nrOfCards": {}}')
    assert b.current == []
    assert b.nrOfPoints == None
    assert len(b.nrOfCards.keys()) == 0