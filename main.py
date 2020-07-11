__version__ = "0.0.5"

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from biddingScreen import BiddingScreen
from specificationScreen import SpecificationScreen

class Manager(ScreenManager):
    biddingScreen = ObjectProperty(None)
    specificationScreen = ObjectProperty(None)

class BridgeBiddingBuddy(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size = (600, 800)
    Window.top = 50

    BridgeBiddingBuddy().run()       