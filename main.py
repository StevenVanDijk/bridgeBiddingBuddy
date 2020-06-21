__version__ = "0.0.4"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from enum import Enum
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.clock import Clock
from bidding import Bidding

class BridgeBiddingBuddy(App):
    # constants
    defaultHeight = 40
    
    bidding = Bidding()
    rootLayout = BoxLayout(orientation='horizontal')

    def getColor(self, txt):
        textColor = [0,1,0,1] 
        if '♣' in txt or '♠' in txt:
            textColor = [0,0,0,1]
        if '♦' in txt or '♥' in txt:
            textColor = [1,0,0,1]
        return textColor

    def buildButton(self, txt, callback):
        btn = Button(color=self.getColor(txt), text=txt, size_hint=(1.0, None),  height=self.defaultHeight * 2, font_name='./consola.ttf')
        btn.bind(on_press=callback)
        return btn

    def buildLabel(self, txt):
        return Label(color=self.getColor(txt), text=txt, size_hint=(1.0, None),  height=self.defaultHeight, font_name='./consola.ttf')

    def onAddBid(self, bid):
        if self.bidding.isAllowed(bid):
            self.bidding.addBid(bid)
        self.updateUI()   

    def onUndo(self):
        self.bidding.removeLastBid()
        self.updateUI()

    def updateUI(self):
        def clearAndBuild(dt):
            self.rootLayout.clear_widgets()
            self.build()

        Clock.schedule_once(clearAndBuild)

    def updateCurrentBidding(self):
        leftLayout = BoxLayout(orientation='vertical')
        def stop_bidding(container):
            def clearBidding(instance):
                self.bidding.reset()
                self.updateUI()

            clearButton = Button(size_hint=(1, None), height=self.defaultHeight, text='next bidding')
            container.add_widget(clearButton)
            clearButton.bind(on_press=clearBidding)

        def rebuilding(container):
            undoBtn = Button(text="Undo", size_hint=(1.0, None), height=self.defaultHeight)
            undoBtn.bind(on_press=lambda ins: self.onUndo())
            container.add_widget(undoBtn)

            currentBidding = GridLayout(cols=4)
            def createCallback(whoStarts):
                return lambda instance: self.bidding.setWhoStarts(whoStarts)

            # create buttons for wind directions
            for elem in self.bidding.playOrder:
                currentBidding.add_widget(self.buildButton(elem, createCallback(elem)))

            # create empty boxes to start at correct starting point
            for i in range(0, self.bidding.playOrder.index(self.bidding.whoStarts)):
                currentBidding.add_widget(self.buildLabel(''))      

            # create labels for all bids  
            for bid in self.bidding.current:
                currentBidding.add_widget(self.buildLabel(bid))
            container.add_widget(currentBidding)

        if self.bidding.finished():
            stop_bidding(leftLayout)
        else:
            rebuilding(leftLayout)

        return leftLayout            

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        leftLayout = self.updateCurrentBidding()
        rightLayout = BoxLayout(orientation='vertical')

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons):
            result = BoxLayout()
            for elem in addedbuttons:
                def createCallback(elem):
                    return lambda instance: self.onAddBid(elem)
                button = self.buildButton(elem, createCallback(elem))
                result.add_widget(button)
            return result            

        # Every row and it's value. Row 0 is the last including pass, X, XX
        bidLayout1 = addButtons(['1♣', '1♦', '1♥', '1♠', '1SA'])
        bidLayout2 = addButtons(['2♣', '2♦', '2♥', '2♠', '2SA'])
        bidLayout3 = addButtons(['3♣', '3♦', '3♥', '3♠', '3SA'])
        bidLayout4 = addButtons(['4♣', '4♦', '4♥', '4♠', '4SA'])
        bidLayout5 = addButtons(['5♣', '5♦', '5♥', '5♠', '5SA'])
        bidLayout6 = addButtons(['6♣', '6♦', '6♥', '6♠', '6SA'])
        bidLayout7 = addButtons(['7♣', '7♦', '7♥', '7♠', '7SA'])
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
        self.rootLayout.add_widget(leftLayout)
        self.rootLayout.add_widget(rightLayout)

        return self.rootLayout

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        