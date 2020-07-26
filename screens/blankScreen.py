from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from mediator import Mediator

# Not a real screen, just used in a workaround to refresh a screen after the viewmodel was updated by mediator

class BlankScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.mediator = mediator

        self.add_widget(self.rootLayout)
        self.build()

    def build(self):
        pass
    
    def onDisplay(self):
        pass