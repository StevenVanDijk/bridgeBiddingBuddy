from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout

from bidding import Bidding, playOrder
from bidding_tree import bids
from constants import clubs, colors, diamonds, hearts, spades
from mediator import Mediator
from uibuilders import (
    ButtonKind, buildButton, buildLabel, buildNumericInput, buildToggle, buildMenu,
    colors, gap, halfGap, smallSize)


class BiddingScreen(Screen):
    currentNumber = None
    currentColor = None
    rootLayout = BoxLayout(orientation='vertical')
    mediator: Mediator

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.mediator = mediator
        self.add_widget(self.rootLayout)
        self.build()

    def onAddBid(self, bid):
        if self.mediator.bidding.isAllowed(bid) and not self.mediator.bidding.finished():
            self.mediator.bidding.addBid(bid)
        self.updateUI()

    def onUndo(self):
        self.mediator.bidding.removeLastBid()
        self.updateUI()

    def setBidding(self, bidding):
        self.mediator.bidding = bidding
        self.updateUI()

    def onDisplay(self):
        self.updateUI()

    def updateUI(self):
        def clearAndBuild(dt):
            self.rootLayout.clear_widgets()
            self.build()

        Clock.schedule_once(clearAndBuild)

    def buildHeaders(self):
        headers = BoxLayout(orientation='vertical')
        topButtons = BoxLayout(orientation='horizontal')

        topButtons.add_widget(buildMenu(self.mediator, size_hint=(0.2, 1.0)))
        topButtons.add_widget(buildButton('Undo', lambda ins: self.onUndo(), size_hint=(0.8, 1.0)))
        headers.add_widget(topButtons)
        suits = GridLayout(cols=4, spacing=[gap, 0], padding=[0, gap])

        def createCallback(whoStarts):
            return lambda instance: self.mediator.bidding.setWhoStarts(whoStarts)

        # create buttons for suits
        if self.mediator.bidding != None:
            for elem in playOrder:
                suits.add_widget(buildToggle(
                    elem, elem == self.mediator.bidding.whoStarts, createCallback(elem), 'whoStarts'))

        headers.add_widget(suits)
        return headers

    def buildCurrentBidding(self):
        currentBidding = GridLayout(cols=4)

        # create empty boxes to start at correct starting point
        numEmpty = playOrder.index(self.mediator.bidding.whoStarts)
        for i in range(0, numEmpty):
            currentBidding.add_widget(buildLabel(''))

        # create labels for all bids
        for bid in self.mediator.bidding.current:
            currentBidding.add_widget(buildLabel(bid))

        # create empty boxes to fill out the screen
        for i in range(0, 32 - len(self.mediator.bidding.current)):
            currentBidding.add_widget(buildLabel(''))

        return currentBidding

    def buildBidChooser(self):
        bidLayout = BoxLayout(orientation='vertical')

        def addButtons(addedbuttons, buttonKind):
            result = BoxLayout(spacing=gap, padding=[0, halfGap])
            for elem in addedbuttons:
                def invoke(elem):
                    if elem == '?':
                        self.mediator.showAdvice()
                        return
                    elif buttonKind == ButtonKind.special:
                        self.onAddBid(elem)
                        return
                    elif buttonKind == ButtonKind.color:
                        self.currentColor = elem
                    elif buttonKind == ButtonKind.number:
                        self.currentNumber = elem
                    if (self.currentNumber != None and self.currentColor != None):
                        self.onAddBid(self.currentNumber + self.currentColor)
                        self.currentColor = self.currentNumber = None

                def createCallback(elem):
                    return lambda instance: invoke(elem)

                def isSelected(elem, buttonKind):
                    if buttonKind == ButtonKind.color:
                        return elem == self.currentColor
                    if buttonKind == ButtonKind.number:
                        return elem == self.currentNumber
                    return False
                result.add_widget(buildToggle(elem, isSelected(
                    elem, buttonKind), createCallback(elem), "buttons_" + str(buttonKind)))
            return result

        numberBtns = addButtons(
            ['1', '2', '3', '4', '5', '6', '7'], ButtonKind.number)
        colorBtns = addButtons(['♣', '♦', '♥', '♠', 'SA'], ButtonKind.color)
        extraBtns = addButtons(['pass', 'X', 'XX', '?'], ButtonKind.special)
        bidLayout.add_widget(numberBtns)
        bidLayout.add_widget(colorBtns)
        bidLayout.add_widget(extraBtns)
        return bidLayout

    def build(self):
        topLayout = BoxLayout(orientation='vertical', size_hint=(1.0, 0.2))
        topLayout.add_widget(self.buildHeaders())

        currentBidding = self.buildCurrentBidding()

        if (not self.mediator.bidding.finished()):
            bottom = BoxLayout(
                orientation='vertical', size_hint=(1.0, 0.3))
            bottom.add_widget(self.buildBidChooser())
        else:
            bottom = buildButton('Klaar', lambda i: self.mediator.closeBidding(), size_hint=(1.0, 0.1))

        self.rootLayout.add_widget(topLayout)
        self.rootLayout.add_widget(currentBidding)
        self.rootLayout.add_widget(bottom)
