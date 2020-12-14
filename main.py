__version__ = "0.0.10"

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition, CardTransition, FallOutTransition

from mediator import (Mediator, adviceScreen, biddingScreen, blankScreen, creditsScreen,
                      fileChooserScreen, specificationScreen)
from screens.adviceScreen import AdviceScreen
from screens.biddingScreen import BiddingScreen
from screens.blankScreen import BlankScree1
from screens.fileChooserScreen import FileChooserScreen
from screens.specificationScreen import SpecificationScreen
from screens.creditsScreen import CreditsScreen

class BridgeBiddingBuddy(App):
    sm = ScreenManager()

    def switchTo(self, name: str):
        if (self.sm.current == name):
            self.sm.transition = NoTransition()
            self.sm.current = blankScreen
        self.sm.current = name
        self.sm.transition = FallOutTransition()

    def build(self):
        mediator = Mediator(self.switchTo)
        for screen in [
                FileChooserScreen(mediator, name=fileChooserScreen),
                BiddingScreen(mediator, name=biddingScreen),
                SpecificationScreen(mediator, name=specificationScreen),
                AdviceScreen(mediator, name=adviceScreen),
                CreditsScreen(mediator, name=creditsScreen),
                BlankScreen(mediator, name=blankScreen)
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
    # Window.size=(720,1280)
    BridgeBiddingBuddy().run()
