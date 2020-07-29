from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from mediator import Mediator
from uibuilders import ButtonKind, buildButton, buildLabel, buildMenu, buildNumericInput, buildText

from constants import colors


class CreditsScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.mediator = mediator

        self.add_widget(self.rootLayout)
        self.reset()

    def build(self):
        self.rootLayout.add_widget(buildMenu(self.mediator, size_hint=(0.2, 0.1)))
        self.rootLayout.add_widget(buildText('''
Bridge Bidding Buddy (BidBud) is gemaakt door de volgende mensen:
 * [b]Marieke van der Valk[/b]: Domein expert en backend developer
 * [b]Steven van Dijk[/b]: Frontend developer
 * [b]Meike van der Valk[/b]: Tester
 * [b]Pepijn van der Valk[/b]: Kleuren
 * [b]Kasper van der Valk[/b]: Tekenen van het BidBud logo 

BidBud is geschreven in [ref=https://www.python.org]Python[/ref] en maakt gebruik van [ref=https://kivy.org]Kivy[/ref].
''', size_hint=(1.0, 0.8)))
        self.rootLayout.add_widget(
            buildButton('Klaar', lambda i: self.mediator.closeSpecification(), size_hint=(1.0, 0.1)))

    def onDisplay(self):
        self.reset()

    def reset(self):
        self.rootLayout.clear_widgets()
        self.build()
