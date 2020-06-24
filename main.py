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

class ButtonKind(Enum):
    number = 1
    color = 2
    special = 3

class BridgeBiddingBuddy(App):
    # constants
    defaultLength = 40
    
    currentNumber = None
    currentColor = None
    bidding = Bidding()
    rootLayout = BoxLayout(orientation='vertical')

    def getColor(self, txt):
        textColor = [0,1,0,1] 
        if '♣' in txt or '♠' in txt:
            textColor = [0,0,0,1]
        if '♦' in txt or '♥' in txt:
            textColor = [1,0,0,1]
        return textColor

    def buildButton(self, txt, callback):
        btn = Button(color=self.getColor(txt), text=txt, size_hint=(1.0, None),  height=self.defaultLength * 2, width=self.defaultLength * 2, font_name='./consola.ttf')
        btn.bind(on_press=callback)
        return btn

    def buildLabel(self, txt):
        return Label(color=self.getColor(txt), text=txt, size_hint=(1.0, None),  height=self.defaultLength, font_name='./consola.ttf')

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

            clearButton = Button(size_hint=(1, None), height=self.defaultLength, text='next bidding')
            container.add_widget(clearButton)
            clearButton.bind(on_press=clearBidding)

        def rebuilding(container):
            undoBtn = Button(text="Undo", size_hint=(1.0, None), height=self.defaultLength)
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
        topLayout = self.updateCurrentBidding()
        bottomLayout = BoxLayout(orientation='vertical')

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons, buttonKind):
            result = BoxLayout()
            for elem in addedbuttons:
                def invoke(elem):
                    if buttonKind == ButtonKind.special: return self.onAddBid(elem)
                    elif buttonKind == ButtonKind.color: self.currentColor = elem
                    elif buttonKind == ButtonKind.number: self.currentNumber = elem
                    if (self.currentNumber != None and self.currentColor != None):
                        self.onAddBid(self.currentNumber + self.currentColor)
                        self.currentColor = self.currentNumber = None
                def createCallback(elem):
                    return lambda instance: invoke(elem)
                button = self.buildButton(elem, createCallback(elem))
                result.add_widget(button)
            return result            

        numberBtns = addButtons(['1', '2', '3', '4', '5', '6', '7'], ButtonKind.number)
        colorBtns = addButtons(['♣', '♦', '♥', '♠', 'SA'], ButtonKind.color)
        extraBtns = addButtons(['pass', 'X', 'XX', '?'], ButtonKind.special)
        bidLayout.add_widget(numberBtns)
        bidLayout.add_widget(colorBtns)
        bidLayout.add_widget(extraBtns)

        bottomLayout.add_widget(bidLayout)
        self.rootLayout.add_widget(topLayout)
        self.rootLayout.add_widget(bottomLayout)

        return self.rootLayout

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size = (600, 800)
    Window.top = 50
    app = BridgeBiddingBuddy()
    app.run()
        