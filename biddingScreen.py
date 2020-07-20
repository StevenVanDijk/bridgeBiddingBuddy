from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import Screen
from uibuilders import buildButton, buildLabel, ButtonKind, buildToggle, buildNumericInput, colors, font_size, smallSize, gap, halfGap
from kivy.clock import Clock
from bidding import Bidding


class BiddingScreen(Screen):
    currentNumber = None
    currentColor = None
    bidding = None
    showQuestions: bool = True
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

    def setBidding(self, bidding):
        self.bidding = bidding
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
            return lambda instance: self.bidding.setWhoStarts(whoStarts)

        # create buttons for suits
        if self.bidding != None:
            for elem in self.bidding.playOrder:
                suits.add_widget(buildToggle(
                    elem, elem == self.bidding.whoStarts, createCallback(elem), 'whoStarts'))

        headers.add_widget(suits)
        return headers

    def buildCurrentBidding(self):
        layout = BoxLayout(orientation='vertical')

        def stop_bidding(container):
            def clearBidding(instance):
                self.bidding.reset()
                self.updateUI()

            container.add_widget(buildButton('next bidding', clearBidding))

        def createQuestionNumberInSuit():
            highestColorLyt = BoxLayout(orientation='horizontal')
            highestColorLyt.add_widget(buildLabel(
                'Nr of cards in suit?', size_hint=(0.6, 1.0)))

            def createCallback(color):
                def cb(instance):
                    self.bidding.setHighestColor(color)
                    self.updateUI()
                return cb

            toggleLyt = GridLayout(cols=4)
            for color in colors:
                toggleLyt.add_widget(buildLabel(color))
            for color in colors:
                def createCallback(color):
                    def cb(instance, value):
                        if value.isdigit(): 
                            newValue = int(value) 
                            if not color in self.bidding.nrOfCards or newValue != self.bidding.nrOfCards[color]:
                                self.bidding.nrOfCards[color] = newValue
                                self.updateUI()
                    return cb
                nrOfCards = buildNumericInput(createCallback(color))
                nrOfCards.text = str(self.bidding.nrOfCards[color]) if color in self.bidding.nrOfCards else ""
                toggleLyt.add_widget(nrOfCards)
            highestColorLyt.add_widget(toggleLyt)

            return highestColorLyt

        def createQuestionNumberOfPoints():
            nrOfPointsLyt = BoxLayout(orientation='horizontal')
            nrOfPointsLyt.add_widget(buildLabel(
                'Nr of points?', size_hint=(0.6, 1.0)))

            def createCallback():
                def cb(instance, value):
                    if (value != ''):
                        nrOfPoints = int(value)
                        if nrOfPoints != self.bidding.nrOfPoints:
                            self.bidding.setNrOfPoints(nrOfPoints)
                            self.updateUI()
                return cb
            nrOfPoints = buildNumericInput(createCallback())
            nrOfPoints.text = str(self.bidding.nrOfPoints) if self.bidding.nrOfPoints != None else ''
            nrOfPointsLyt.add_widget(nrOfPoints)

            return nrOfPointsLyt

        def show_questions(container):
            questions = BoxLayout(orientation='vertical')
            questions.add_widget(createQuestionNumberOfPoints())
            questions.add_widget(createQuestionNumberInSuit())
            def cb(instance):
                self.showQuestions = False
                self.updateUI()
            questions.add_widget(buildButton("Close", cb))
            container.add_widget(questions)

        def show_bidding(container):
            currentBidding = GridLayout(cols=4)

            # create empty boxes to start at correct starting point
            numEmpty = self.bidding.playOrder.index(self.bidding.whoStarts)
            for i in range(0, numEmpty):
                currentBidding.add_widget(buildLabel(''))

            # create labels for all bids
            for bid in self.bidding.current:
                currentBidding.add_widget(buildLabel(bid))

            # create empty boxes to fill out the row
            for i in range(0, 4 - (numEmpty + len(self.bidding.current)) % 4):
                currentBidding.add_widget(buildLabel(''))

            container.add_widget(currentBidding)

        if self.bidding == None or self.bidding.finished():
            stop_bidding(layout)
        else:
            if (self.showQuestions or self.bidding.nrOfPoints == None or not all([color in self.bidding.nrOfCards for color in colors])):
                show_questions(layout)
            else:
                show_bidding(layout)

        return layout

    def buildBidChooser(self):
        bidLayout = BoxLayout(orientation='vertical')

        def addButtons(addedbuttons, buttonKind):
            result = BoxLayout(spacing=gap, padding=[0, halfGap])
            for elem in addedbuttons:
                def invoke(elem):
                    if elem == '?':
                        return self.manager.switch_to(self.manager.specificationScreen)
                    if buttonKind == ButtonKind.special:
                        return self.onAddBid(elem)
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

        bottomLayout = BoxLayout(orientation='vertical', size_hint=(1.0, 0.3))
        bottomLayout.add_widget(self.buildBidChooser())

        self.rootLayout.add_widget(topLayout)
        self.rootLayout.add_widget(currentBidding)
        self.rootLayout.add_widget(bottomLayout)
