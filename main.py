from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from enum import Enum

class BridgeBiddingBuddy(App):
    currentBidding = None

    def build(self):
        self.currentBidding = GridLayout(cols=4)
        
        rootLayout = BoxLayout()
        rootLayout.add_widget(self.currentBidding)
        return rootLayout

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        