from kivy.uix.screenmanager import ScreenManager
from bidding import Bidding

class Mediator():
    manager: ScreenManager
    bidding: Bidding = Bidding()

    def __init__(self, manager):
        self.manager = manager

    def setBidding(self, bidding):
        self.bidding = bidding