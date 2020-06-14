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
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.clock import Clock

class BridgeBiddingBuddy(App):
    # constants
    defaultHeight = 40
    playOrder = ["N", "E", "S", "W"]
    buttonsDict = {
        '1♣': 1, '2♣': 4, '3♣': 9, '4♣': 14, '5♣': 19, '6♣': 24, '7♣': 29,
        '1♦': 2, '2♦': 5, '3♦': 10, '4♦': 15, '5♦': 20, '6♦': 25, '7♦': 30,
        '1♥': 3, '2♥': 6, '3♥': 11, '4♥': 16, '5♥': 21, '6♥': 26, '7♥': 31,
        '1♠': 4, '2♠': 7, '3♠': 12, '4♠': 17, '5♠': 22, '6♠': 27, '7♠': 32,
        '1SA': 5, '2SA': 8, '3SA': 13, '4SA': 18, '5SA': 23, '6SA': 28, '7SA': 33
    }

    currentBidding = []
    leftLayout: BoxLayout = None
    whoStarts = 'N'
    bidding_ended = False


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

    def isSpecial(self, bid):
        return bid == 'pass' or bid == 'X' or bid == 'XX'

    def getLastBidOrder(self):
        previousBids = [elem for elem in self.currentBidding if not self.isSpecial(elem)]
        if len(previousBids) > 0:
            return self.buttonsDict[previousBids.pop()]
        else:
            return -1

    def onAddBid(self, bid):
        if not self.bidding_ended:
            if not self.isSpecial(bid):
                if self.buttonsDict[bid] <= self.getLastBidOrder():
                    return
            self.currentBidding.append(bid)
        self.scheduleUpdateCurrentBidding()   

    def onUndo(self):
        self.bidding_ended = False
        if len(self.currentBidding) > 0: 
            self.currentBidding.pop()
        self.scheduleUpdateCurrentBidding()

    def setWhoStarts(self, whoStarts):
        if (len(self.currentBidding) == 0): 
            self.whoStarts = whoStarts

    def clearBidding(self, instance):
        self.currentBidding.clear()
        
    def scheduleUpdateCurrentBidding(self):
        Clock.schedule_once(self.updateCurrentBidding())

    def updateCurrentBidding(self):
        def stop_bidding():
            def clearBidding(instance):
                self.updateCurrentBidding()
                self.currentBidding.clear()

            self.bidding_ended = True    
            text = 'next bidding'    
            clearButton = Button(size_hint=(1, None), height=self.defaultHeight, text=text)
            self.leftLayout.add_widget(clearButton)
            clearButton.bind(on_press= clearBidding)

        def rebuilding():
            undoBtn = Button(text="Undo", size_hint=(1.0, None), height=self.defaultHeight)
            undoBtn.bind(on_press=lambda ins: self.onUndo())
            self.leftLayout.add_widget(undoBtn)

            currentBidding = GridLayout(cols=4)
            def createCallback(whoStarts):
                return lambda instance: self.setWhoStarts(whoStarts)
            # create buttons for wind directions
            for elem in self.playOrder:
                currentBidding.add_widget(self.buildButton(elem, createCallback(elem)))

            # create empty boxes to start at correct starting point
            for i in range(0, self.playOrder.index(self.whoStarts)):
                currentBidding.add_widget(self.buildLabel(''))      

            # create labels for all bids  
            for bid in self.currentBidding:
                currentBidding.add_widget(self.buildLabel(bid))
            self.leftLayout.add_widget(currentBidding)

        self.leftLayout.clear_widgets()

        count_biddings = len(self.currentBidding)
        if count_biddings >= 4:
            if self.currentBidding[-1] == 'pass' and self.currentBidding[-2] == 'pass' and self.currentBidding[-3] == 'pass':
                rebuilding()
                stop_bidding() 
            else:
                rebuilding()   
        else:
            rebuilding()
            

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        rootLayout = BoxLayout(orientation='horizontal')
        self.leftLayout = BoxLayout(orientation='vertical')
        rightLayout = BoxLayout(orientation='vertical')

        self.updateCurrentBidding()

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons):
            result = BoxLayout()
            for elem in addedbuttons:
                def createCallback(elem):
                    return lambda instance: self.onAddBid(elem)
                AButton = self.buildButton(elem, createCallback(elem))
                self.lastBid = elem
                result.add_widget(AButton)
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
        rootLayout.add_widget(self.leftLayout)
        rootLayout.add_widget(rightLayout)

        return rootLayout

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        