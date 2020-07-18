from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from uibuilders import buildButton, buildLabel, ButtonKind


class SpecificationScreen(Screen):
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.add_widget(self.rootLayout)
        self.build()

    def build(self):
        pass
