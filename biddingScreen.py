from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from uibuilders import buildButton, buildLabel, ButtonKind
from kivy.clock import Clock
from bidding import Bidding

class BiddingScreen(Screen):    
    currentNumber = None
    currentColor = None
    bidding = Bidding()
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.add_widget(self.rootLayout)
        self.build()
        
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
        layout = BoxLayout(orientation='vertical')
        def stop_bidding(container):
            def clearBidding(instance):
                self.bidding.reset()
                self.updateUI()

            container.add_widget(buildButton('next bidding', clearBidding))

        def show_bidding(container):
            container.add_widget(buildButton('Undo', lambda ins: self.onUndo()))

            currentBidding = GridLayout(cols=4)
            def createCallback(whoStarts):
                return lambda instance: self.bidding.setWhoStarts(whoStarts)

            # create buttons for wind directions
            for elem in self.bidding.playOrder:
                currentBidding.add_widget(buildButton(elem, createCallback(elem)))

            # create empty boxes to start at correct starting point
            for i in range(0, self.bidding.playOrder.index(self.bidding.whoStarts)):
                currentBidding.add_widget(buildLabel(''))      

            # create labels for all bids  
            for bid in self.bidding.current:
                currentBidding.add_widget(buildLabel(bid))
            container.add_widget(currentBidding)

        if self.bidding.finished():
            stop_bidding(layout)
        else:
            show_bidding(layout)

        return layout            

    def build(self):
        topLayout = self.updateCurrentBidding()
        bottomLayout = BoxLayout(orientation='vertical', size_hint=(1.0, 0.3))

        bidLayout = BoxLayout(orientation='vertical')
        def addButtons(addedbuttons, buttonKind):
            result = BoxLayout()
            for elem in addedbuttons:
                def invoke(elem):                    
                    if elem == '?': return self.manager.switch_to(self.manager.specificationScreen)
                    if buttonKind == ButtonKind.special: return self.onAddBid(elem)
                    elif buttonKind == ButtonKind.color: self.currentColor = elem
                    elif buttonKind == ButtonKind.number: self.currentNumber = elem
                    if (self.currentNumber != None and self.currentColor != None):
                        self.onAddBid(self.currentNumber + self.currentColor)
                        self.currentColor = self.currentNumber = None
                def createCallback(elem):
                    return lambda instance: invoke(elem)
                result.add_widget(buildButton(elem, createCallback(elem)))
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
