import json
from bidding import Bidding


class BiddingEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Bidding):
            result = {
                "current": obj.current,
                "whoStarts": obj.whoStarts,
                "nrOfPoints": obj.nrOfPoints,
                "nrOfCards": obj.nrOfCards
            }
            return result
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
