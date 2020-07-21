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
    mediator = Mediator()
    biddingScreen = BiddingScreen(mediator, name='biddingScreen')
    fileChooserScreen = FileChooserScreen(name='fileChooserScreen')

    def build(self):
        sm = Manager()
        sm.add_widget(self.biddingScreen)
        sm.add_widget(self.fileChooserScreen)
        sm.add_widget(SpecificationScreen(name='specificationScreen'))
        return sm


if __name__ == '__main__':
    Window.clearcolor = (.5, .5, .5, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
