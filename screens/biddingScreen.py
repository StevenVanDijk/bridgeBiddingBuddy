from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout

from bidding import Bidding
from bidding_tree import bids
from constants import clubs, colors, diamonds, hearts, spades
from mediator import Mediator
from uibuilders import (
    ButtonKind, buildButton, buildLabel, buildNumericInput, buildToggle,
    colors, font_size, gap, halfGap, smallSize)


class BiddingScreen(Screen):
    currentNumber = None
    currentColor = None
    showQuestions: bool = True
    rootLayout = BoxLayout(orientation='vertical')
    mediator: Mediator

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.mediator = mediator
        self.add_widget(self.rootLayout)
        self.build()

    def onAddBid(self, bid):
        if self.mediator.bidding.isAllowed(bid):
            self.mediator.bidding.addBid(bid)
            if (self.mediator.bidding.finished()):
                self.mediator.closeBidding()
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

        def cb(instance):
            self.showQuestions = True
            self.updateUI()
        topButtons.add_widget(buildButton('Q', cb, size_hint=(0.2, 1.0)))
        topButtons.add_widget(buildButton('Undo', lambda ins: self.onUndo()))
        headers.add_widget(topButtons)
        suits = GridLayout(cols=4, spacing=[gap, 0], padding=[0, gap])

        def createCallback(whoStarts):
            return lambda instance: self.mediator.bidding.setWhoStarts(whoStarts)

        # create buttons for suits
        if self.mediator.bidding != None:
            for elem in self.mediator.bidding.playOrder:
                suits.add_widget(buildToggle(
                    elem, elem == self.mediator.bidding.whoStarts, createCallback(elem), 'whoStarts'))

        headers.add_widget(suits)
        return headers

    def buildQuestions(self):
        def createQuestionNumberInSuit():
            container = BoxLayout(orientation='vertical', size_hint=(1.0, 0.2))
            suitsLyt = BoxLayout(orientation='horizontal', size_hint=(0.6, 1.0), pos_hint={'right': 1
                                                                                           })
            for color in colors:
                suitsLyt.add_widget(buildLabel(color))
            container.add_widget(suitsLyt)

            bottomLyt = BoxLayout(orientation='horizontal')
            bottomLyt.add_widget(buildLabel(
                'Nr of cards in suit?', size_hint=(0.6, 1.0)))

            numEntriesLyt = BoxLayout(
                orientation='horizontal', size_hint=(1.0, 1.0))

            for color in colors:
                def createCallback(color):
                    def cb(instance, value):
                        if value.isdigit():
                            newValue = int(value)
                            if not color in self.mediator.bidding.nrOfCards or newValue != self.mediator.bidding.nrOfCards[color]:
                                self.mediator.bidding.nrOfCards[color] = newValue
                                self.updateUI()
                    return cb
                nrOfCards = buildNumericInput(createCallback(color))
                nrOfCards.text = str(
                    self.mediator.bidding.nrOfCards[color]) if color in self.mediator.bidding.nrOfCards else ""
                numEntriesLyt.add_widget(nrOfCards)
            bottomLyt.add_widget(numEntriesLyt)
            container.add_widget(bottomLyt)

            return container

        def createQuestionNumberOfPoints():
            nrOfPointsLyt = BoxLayout(
                orientation='horizontal', size_hint=(1.0, 0.1))
            nrOfPointsLyt.add_widget(buildLabel(
                'Nr of points?', size_hint=(0.6, 1.0)))

            def createCallback():
                def cb(instance, value):
                    if (value != ''):
                        nrOfPoints = int(value)
                        if nrOfPoints != self.mediator.bidding.nrOfPoints:
                            self.mediator.bidding.setNrOfPoints(nrOfPoints)
                            self.updateUI()
                return cb
            nrOfPoints = buildNumericInput(createCallback())
            nrOfPoints.text = str(
                self.mediator.bidding.nrOfPoints) if self.mediator.bidding.nrOfPoints != None else ''
            nrOfPointsLyt.add_widget(nrOfPoints)

            return nrOfPointsLyt
        questions = BoxLayout(orientation='vertical')
        questions.add_widget(buildLabel(
            "Please enter some information about your own hand.", size_hint=(1.0, 0.1)))
        questions.add_widget(BoxLayout())  # empty space
        if self.mediator.bidding != None:
            questions.add_widget(createQuestionNumberOfPoints())
            questions.add_widget(createQuestionNumberInSuit())

        def cb(instance):
            self.showQuestions = False
            self.updateUI()
        questions.add_widget(BoxLayout())  # empty space
        questions.add_widget(buildButton("Close", cb, size_hint=(1.0, 0.1)))
        return questions

    def buildCurrentBidding(self):
        currentBidding = GridLayout(cols=4)

        # create empty boxes to start at correct starting point
        numEmpty = self.mediator.bidding.playOrder.index(
            self.mediator.bidding.whoStarts)
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
        if (self.showQuestions or self.mediator.bidding.nrOfPoints == None or not all([color in self.mediator.bidding.nrOfCards for color in colors])):
            self.rootLayout.add_widget(self.buildQuestions())
        else:
            topLayout = BoxLayout(orientation='vertical', size_hint=(1.0, 0.2))
            topLayout.add_widget(self.buildHeaders())

            currentBidding = self.buildCurrentBidding()

            bottomLayout = BoxLayout(
                orientation='vertical', size_hint=(1.0, 0.3))
            bottomLayout.add_widget(self.buildBidChooser())

            self.rootLayout.add_widget(topLayout)
            self.rootLayout.add_widget(currentBidding)
            self.rootLayout.add_widget(bottomLayout)
