from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from uibuilders import buildButton, buildLabel, ButtonKind, buildText, buildHugeLabel
from mediator import Mediator

class AdviceScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.mediator = mediator

        self.add_widget(self.rootLayout)
        self.reset()

    def build(self):
        (bid, explanation) = self.mediator.advice
        adviceLabel = buildHugeLabel(bid, size_hint=(1.0, 0.1))
        self.rootLayout.add_widget(adviceLabel)
        self.rootLayout.add_widget(buildText(explanation, size_hint=(1.0, 0.8)))
        self.rootLayout.add_widget(buildButton('Klaar', lambda i: self.mediator.closeAdvice(), size_hint=(1.0, 0.1)))

    def reset(self):
        self.rootLayout.clear_widgets()
        if (self.mediator.advice != None):
            self.build()

    def onDisplay(self):
        self.reset()