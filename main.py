__version__ = "0.0.6"

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from biddingScreen import BiddingScreen
from specificationScreen import SpecificationScreen
from fileChooserScreen import FileChooserScreen
from adviceScreen import AdviceScreen
from bidding import Bidding
from mediator import Mediator, biddingScreen, fileChooserScreen, specificationScreen, adviceScreen


class BridgeBiddingBuddy(App):
    sm = ScreenManager()
    mediator = Mediator(sm)
    biddingScreen = BiddingScreen(mediator, name=biddingScreen)
    specificationScreen = SpecificationScreen(mediator, name=specificationScreen)
    adviceScreen = AdviceScreen(mediator, name=adviceScreen)
    fileChooserScreen = FileChooserScreen(mediator, name=fileChooserScreen)

    def build(self):
        for screen in [self.biddingScreen, self.fileChooserScreen, self.specificationScreen, self.adviceScreen]:
            self.sm.add_widget(screen)
            screen.bind(on_pre_enter=lambda i: screen.onDisplay())
        return self.sm


if __name__ == '__main__':
    Window.clearcolor = (.5, .5, .5, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
