__version__ = "0.0.6"

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from biddingScreen import BiddingScreen
from specificationScreen import SpecificationScreen
from fileChooserScreen import FileChooserScreen
from bidding import Bidding
from mediator import Mediator


class Manager(ScreenManager):
    pass


class BridgeBiddingBuddy(App):
    sm = Manager()
    mediator = Mediator(sm)
    biddingScreen = BiddingScreen(mediator, name='biddingScreen')
    fileChooserScreen = FileChooserScreen(mediator, name='fileChooserScreen')
    specificationScreen = SpecificationScreen(mediator, name='specificationScreen')

    def build(self):
        self.sm.add_widget(self.fileChooserScreen)
        self.sm.add_widget(self.biddingScreen)
        self.sm.add_widget(self.specificationScreen)
        return self.sm


if __name__ == '__main__':
    Window.clearcolor = (.5, .5, .5, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
