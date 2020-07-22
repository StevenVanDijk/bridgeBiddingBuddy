from kivy.uix.screenmanager import ScreenManager
from bidding import Bidding
from bidding_tree import bids
from constants import spades, hearts, clubs, diamonds
from uibuilders import colors

biddingScreen = 'biddingScreen'
fileChooserScreen = 'fileChooserScreen'
specificationScreen = 'specificationScreen'
adviceScreen = 'adviceScreen'

class Mediator():
    manager: ScreenManager
    bidding: Bidding = Bidding()
    advice: str = None

    def __init__(self, manager):
        self.manager = manager
        self.setBidding(Bidding())

    def setBidding(self, bidding):
        bidding.nrOfPoints = 12
        bidding.nrOfCards = {}
        for color in colors:
            bidding.nrOfCards[color] = 2
        self.bidding = bidding

    def showAdvice(self):
        cards = self.bidding.nrOfCards
        print("('autogenerated', %s, %d, %d, %d, %d, %d, '???')" % (str(self.bidding.current), self.bidding.nrOfPoints,
                                                                    cards[spades], cards[hearts], cards[diamonds], cards[clubs]))
        self.advice = bids(self.bidding.current, self.bidding.nrOfPoints,
                           cards[spades], cards[hearts], cards[diamonds], cards[clubs])
        
        self.manager.current = adviceScreen

    def closeAdvice(self):
        self.manager.current = biddingScreen
