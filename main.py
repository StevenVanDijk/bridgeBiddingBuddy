__version__ = "0.0.6"

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mediator import (
    Mediator, adviceScreen, biddingScreen, fileChooserScreen,
    specificationScreen)
from screens.adviceScreen import AdviceScreen
from screens.biddingScreen import BiddingScreen
from screens.fileChooserScreen import FileChooserScreen
from screens.specificationScreen import SpecificationScreen


class BridgeBiddingBuddy(App):
    sm = ScreenManager()

    def switchTo(self, name: str):
        self.sm.current = name

    def build(self):
        mediator = Mediator(self.switchTo)
        for screen in [
            FileChooserScreen(mediator, name=fileChooserScreen),
            BiddingScreen(mediator, name=biddingScreen),
            SpecificationScreen(mediator, name=specificationScreen),
            AdviceScreen(mediator, name=adviceScreen)
        ]:
            self.sm.add_widget(screen)

            def createCallback(screen):
                def cb(instance):
                    screen.onDisplay()
                return cb
            screen.bind(on_pre_enter=createCallback(screen))
        return self.sm


if __name__ == '__main__':
    Window.clearcolor = (.5, .5, .5, 1)
    Window.size = (500, 700)
    Window.top = 50

    BridgeBiddingBuddy().run()
