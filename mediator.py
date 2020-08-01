import re
from typing import Callable

from kivy.storage.jsonstore import JsonStore

from bidding import Bidding
from biddingEncoder import json2Bid, bid2Json
from bidding_tree import bids
from constants import clubs, diamonds, hearts, spades, colors
from uitleg import uitleg_nl
from datetime import datetime

from uuid import uuid4

biddingScreen = 'biddingScreen'
fileChooserScreen = 'fileChooserScreen'
specificationScreen = 'specificationScreen'
adviceScreen = 'adviceScreen'
creditsScreen = 'creditsScreen'
blankScreen = 'blankScreen'


class Mediator():
    bidding: Bidding = Bidding()
    advice: str = None

    __storage = JsonStore('allbids.json')
    __patternExplanation = re.compile('\n[\t ]+')
    __switchTo: Callable[[str], None]

    def __init__(self, switchTo):
        self.__switchTo = switchTo

    def getBiddingKeys(self):
        keys = self.__storage.keys()
        return [ (key, self.__storage.get(key)["name"], self.__storage.get(key)["contract"]) for key in keys ]

    def setBidding(self, bidding: Bidding):
        self.bidding = bidding

    def showAdvice(self):
        cards = self.bidding.nrOfCards
        print("('autogenerated', %s, %d, %d, %d, %d, %d, '???', '???')" %
              (str(self.bidding.current), self.bidding.nrOfPoints,
               cards[spades], cards[hearts], cards[diamonds], cards[clubs]))
        (bid, explainTag) = bids(self.bidding.current, self.bidding.nrOfPoints,
                                 cards[spades], cards[hearts], cards[diamonds],
                                 cards[clubs])
        explanation = uitleg_nl(explainTag).replace("\t", "")
        cleaned = re.sub(self.__patternExplanation, '\n\n', explanation)
        self.advice = (bid, cleaned)

        self.__switchTo(adviceScreen)

    def closeAdvice(self):
        self.__switchTo(biddingScreen)

    def editBidding(self, bidding: Bidding):
        self.setBidding(bidding)
        if (bidding.needsSpecification()):
            self.__switchTo(specificationScreen)
        else:
            self.__switchTo(biddingScreen)

    def closeBidding(self):
        key = uuid4().hex
        name = "Bidding at " + datetime.now().strftime("%c")
        value = bid2Json(self.bidding)
        (contract, leader) = self.bidding.contract()
        self.__storage.put(key, name=name, bid=value, contract=contract + " " + leader )
        self.__switchTo(fileChooserScreen)

    def loadBidding(self, key):
        bidding = json2Bid(self.__storage.get(key)['bid'])
        self.editBidding(bidding)

    def deleteBidding(self, key):
        self.__storage.delete(key)
        self.__switchTo(fileChooserScreen)

    def changeBiddingName(self, key, value):
        self.__storage.put(key, bid=self.__storage.get(key)['bid'], contract=self.__storage.get(key)['contract'], name=value)
        self.__switchTo(fileChooserScreen)

    def showSpecification(self):
        self.__switchTo(specificationScreen)

    def closeSpecification(self):
        if (not self.bidding.needsSpecification()):
            self.__switchTo(biddingScreen)

    def showBiddingChooser(self):
        self.__switchTo(fileChooserScreen)
    
    def showCredits(self):
        self.__switchTo(creditsScreen)