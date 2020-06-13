from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from enum import Enum
from kivy.uix.anchorlayout import AnchorLayout

class BridgeBiddingBuddy(App):
    currentBidding = None
    defaultHeight = 50
    value = 0
    lastBid = ''
    buttonsDict = {
        '1♣': 1, '2♣': 5, '3♣': 9, '4♣': 13, '5♣': 17, '6♣': 21, '7♣': 25,
        '1♦': 2, '2♦': 6, '3♦': 10, '4♦': 14, '5♦': 18, '6♦': 22, '7♦': 26,
        '1♥': 3, '2♥': 7, '3♥': 11, '4♥': 15, '5♥': 19, '6♥': 23, '7♥': 27,
        '1♠': 4, '2♠': 8, '3♠': 12, '4♠': 16, '5♠': 20, '6♠': 24, '7♠': 28  
    }

    def buildLabel(self, txt):
        return Label(text=txt, size_hint=(1.0, None),  height=self.defaultHeight)

    def onAddBid(self, bid):
        if bid > self.lastBid:
            self.lastBid = bid
            self.currentBidding.add_widget(self.buildLabel(bid))

    def build(self):
        rootLayout = BoxLayout(orientation='horizontal')
        leftLayout = BoxLayout(orientation='vertical')
        rightLayout = BoxLayout(orientation='vertical')

        self.currentBidding = GridLayout(cols=4)
        for elem in ["N", "E", "S", "W"]:
            self.currentBidding.add_widget(self.buildLabel(elem))        
        leftLayout.add_widget(self.currentBidding)

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons):
            result = BoxLayout()
            for elem in addedbuttons:
                AButton = Button(text=elem)
                def createCallback(elem):
                    return lambda instance: self.onAddBid(elem)
                AButton.bind(on_press=createCallback(elem))
                self.lastBid = elem
                result.add_widget(AButton)
            return result            

        # Every row and it's value. Row 0 is the last including pass, X, XX
        bidLayout1 = addButtons(['1♣', '1♦', '1♥', '1♠'])
        bidLayout2 = addButtons(['2♣', '2♦', '2♥', '2♠'])
        bidLayout3 = addButtons(['3♣', '3♦', '3♥', '3♠'])
        bidLayout4 = addButtons(['4♣', '4♦', '4♥', '4♠'])
        bidLayout5 = addButtons(['5♣', '5♦', '5♥', '5♠'])
        bidLayout6 = addButtons(['6♣', '6♦', '6♥', '6♠'])
        bidLayout7 = addButtons(['7♣', '7♦', '7♥', '7♠'])
        bidLayout0 = addButtons(['pass', 'X', 'XX'])

        bidLayout.add_widget(bidLayout1)
        bidLayout.add_widget(bidLayout2)
        bidLayout.add_widget(bidLayout3)
        bidLayout.add_widget(bidLayout4)
        bidLayout.add_widget(bidLayout5)
        bidLayout.add_widget(bidLayout6)
        bidLayout.add_widget(bidLayout7)
        bidLayout.add_widget(bidLayout0)

        rightLayout.add_widget(bidLayout)
        rootLayout.add_widget(leftLayout)
        rootLayout.add_widget(rightLayout)

        return rootLayout

            

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        