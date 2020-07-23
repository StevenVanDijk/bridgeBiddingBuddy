from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from uibuilders import buildButton, buildLabel, ButtonKind
from mediator import Mediator


class SpecificationScreen(Screen):
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