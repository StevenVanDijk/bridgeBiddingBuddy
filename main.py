__version__ = "0.0.6"

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from biddingScreen import BiddingScreen
from specificationScreen import SpecificationScreen
from bidding import Bidding


class Manager(ScreenManager):
    pass


class BridgeBiddingBuddy(App):
    bidding = Bidding()
    biddingScreen = BiddingScreen(name='biddingScreen')

    def build(self):
        sm = Manager()
        sm.add_widget(self.biddingScreen)
        sm.add_widget(SpecificationScreen(name='specificationScreen'))
        self.biddingScreen.setBidding(self.bidding)
        return sm


if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
