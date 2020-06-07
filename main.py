from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from enum import Enum

class BridgeBiddingBuddy(App):
    currentBidding = None

    def ts(self, symb):
        if symb == k:
            return '♣'
        if symb == r:
            return '♦'
        if symb == h:
            return '♥'
        if symb == s:
            return '♠'

    def build(self):
        self.currentBidding = GridLayout(cols=4)
        
        bidLayout = BoxLayout()
        def addButtons(addedbuttons):
            result = BoxLayout()
            for elem in addedbuttons:
                AButton = Button(text=elem)
                AButton = elem
                result.add_widget(AButton)
            return result
            

        # Every row and it's value. Row 0 is the last including pass, X, XX
        bidLayout1 = addButtons(['1kl', '1ru', '1ha', '1sc'])
        bidLayout2 = None
        bidLayout3 = None
        bidLayout4 = None
        bidLayout5 = None
        bidLayout6 = None
        bidLayout7 = None
        bidLayout0 = None

        bidLayout.add_widget(bidLayout1)

        rootLayout = BoxLayout()
        rootLayout.add_widget(self.currentBidding)
        return rootLayout

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        