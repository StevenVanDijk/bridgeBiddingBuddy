import json
from bidding import Bidding


class BiddingEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Bidding):
            result = {
                "__type__": "Bidding",
                "current": obj.current,
                "whoStarts": obj.whoStarts,
                "nrOfPoints": obj.nrOfPoints,
                "nrOfCards": obj.nrOfCards
            }
            return result
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def bidToJson(bid: Bidding) -> str:
    return json.dumps(bid, cls=BiddingEncoder, ensure_ascii=False)

def json2Bid(jsonStr: str) -> Bidding:
    def bidBuilder(dictionary: dict) -> Bidding:
        if "__type__" in dictionary and dictionary["__type__"] == "Bidding":
            result = Bidding()
            result.current = dictionary["current"]
            result.whoStarts = dictionary["whoStarts"]
            result.nrOfPoints = dictionary["nrOfPoints"]
            result.nrOfCards = dictionary["nrOfCards"]
            return result
        else:
            return dictionary

    return json.loads(jsonStr, object_hook=bidBuilder)