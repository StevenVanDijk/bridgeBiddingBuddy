__version__ = "0.0.6"

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from screens.biddingScreen import BiddingScreen
from screens.specificationScreen import SpecificationScreen
from screens.fileChooserScreen import FileChooserScreen
from screens.adviceScreen import AdviceScreen
from mediator import Mediator, biddingScreen, fileChooserScreen, specificationScreen, adviceScreen


class BridgeBiddingBuddy(App):
    def build(self):
        sm = ScreenManager()
        mediator = Mediator(sm)
        for screen in [
            BiddingScreen(mediator, name=biddingScreen), 
            FileChooserScreen(mediator, name=fileChooserScreen), 
            SpecificationScreen(mediator, name=specificationScreen), 
            AdviceScreen(mediator, name=adviceScreen)
        ]:
            sm.add_widget(screen)
            def createCallback(screen): 
                def cb(instance):
                    screen.onDisplay()
                return cb
            screen.bind(on_pre_enter=createCallback(screen))
        return sm


if __name__ == '__main__':
    Window.clearcolor = (.5, .5, .5, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
