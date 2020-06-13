from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from enum import Enum

class BridgeBiddingBuddy(App):
    currentBidding = None
    defaultHeight = 50

    def buildLabel(self, txt):
        return Label(text=txt, size_hint=(1.0, None),  height=self.defaultHeight)

    def onAddBid(self, value):
        self.currentBidding.add_widget(self.buildLabel(value))

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
                result.add_widget(AButton)
            return result            

        # Every row and it's value. Row 0 is the last including pass, X, XX
        bidLayout1 = addButtons(['1kl', '1ru', '1ha', '1sc'])
        bidLayout2 = addButtons(['2kl', '2ru', '2ha', '2sc'])
        bidLayout3 = addButtons(['3kl', '3ru', '3ha', '3sc'])
        bidLayout4 = addButtons(['4kl', '4ru', '4ha', '4sc'])
        bidLayout5 = addButtons(['5kl', '5ru', '5ha', '5sc'])
        bidLayout6 = addButtons(['6kl', '6ru', '6ha', '6sc'])
        bidLayout7 = addButtons(['7kl', '7ru', '7ha', '7sc'])
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
        