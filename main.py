from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from enum import Enum
from kivy.uix.anchorlayout import AnchorLayout

class BridgeBiddingBuddy(App):
    currentBidding = None
    defaultHeight = 50

    def onAddBid(self, value):
        self.currentBidding.add_widget(Label(text=value))


    def build(self):
        rootLayout = BoxLayout(orientation='horizontal')
        leftLayout = BoxLayout(orientation='vertical')
        rightLayout = BoxLayout(orientation='vertical')

        NOSWlayout = AnchorLayout(
            anchor_x='center', anchor_y='top')
        for elem in ["N", "E", "S", "W"]:
            NOSWlayout.add_widget(Label(text=elem))


        
       

        self.currentBidding = GridLayout(cols=4, size_hint=(1.0, None), height=self.defaultHeight)
        
        leftLayout.add_widget(NOSWlayout)
        leftLayout.add_widget(self.currentBidding)

        self.bidTxt = TextInput(text='', multiline=False)
        self.bidTxt.bind(on_text_validate=lambda instance: self.onAddBid(instance))
        rightLayout.add_widget(self.bidTxt)

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons):
            result = BoxLayout()
            for elem in addedbuttons:
                AButton = Button(text=elem)
                AButton.bind(on_press=lambda instance: self.onAddBid(elem))
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
        