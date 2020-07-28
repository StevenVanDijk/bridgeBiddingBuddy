from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from mediator import Mediator
from uibuilders import ButtonKind, buildButton, buildLabel, buildMenu, buildNumericInput

from constants import colors


class SpecificationScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.mediator = mediator

        self.add_widget(self.rootLayout)
        self.reset()

    def buildQuestions(self):
        def buildNumberInSuit():
            result = []
            for color in colors:
                result.append(buildLabel(color))

                def createCallback(color):
                    def cb(instance, value):
                        if value.isdigit():
                            newValue = int(value)
                            if not color in self.mediator.bidding.nrOfCards or newValue != self.mediator.bidding.nrOfCards[
                                    color]:
                                self.mediator.bidding.nrOfCards[color] = newValue

                    return cb

                initialValue = str(
                    self.mediator.bidding.nrOfCards[color]) if color in self.mediator.bidding.nrOfCards else ""
                nrOfCards = buildNumericInput(initialValue, createCallback(color))
                result.append(nrOfCards)

            return result

        def buildInputNumberOfPoints():
            def createCallback():
                def cb(instance, value):
                    if (value != ''):
                        nrOfPoints = int(value)
                        if nrOfPoints != self.mediator.bidding.nrOfPoints:
                            self.mediator.bidding.setNrOfPoints(nrOfPoints)

                return cb

            initialValue = str(self.mediator.bidding.nrOfPoints) if self.mediator.bidding.nrOfPoints != None else ''
            nrOfPoints = buildNumericInput(initialValue, createCallback())

            return nrOfPoints

        questions = BoxLayout(orientation='vertical')
        questions.add_widget(buildLabel("Please enter some information\nabout your own hand.", size_hint=(1.0, 0.1)))

        gridLyt = GridLayout(cols=2)
        gridLyt.add_widget(buildLabel('Points'))
        gridLyt.add_widget(buildInputNumberOfPoints())
        for w in buildNumberInSuit():
            gridLyt.add_widget(w)

        questions.add_widget(gridLyt)
        
        return questions

    def build(self):
        self.rootLayout.add_widget(buildMenu(self.mediator, size_hint=(0.2, 0.1)))
        self.rootLayout.add_widget(self.buildQuestions())
        self.rootLayout.add_widget(
            buildButton('Done', lambda i: self.mediator.closeSpecification(), size_hint=(1.0, 0.1)))

    def onDisplay(self):
        self.reset()

    def reset(self):
        self.rootLayout.clear_widgets()
        self.build()
