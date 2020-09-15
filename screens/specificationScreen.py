from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from mediator import Mediator
from uibuilders import ButtonKind, buildButton, buildLabel, buildMenu, buildNumericInput, buildText

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
                result.append(buildLabel('Aantal kaarten in' + ' ' + color))

                def createSetterCallback(color):
                    def cb(instance, value):
                        if not color in self.mediator.bidding.nrOfCards or value != self.mediator.bidding.nrOfCards[
                                color]:
                            self.mediator.bidding.nrOfCards[color] = value

                    return cb

                def createValidationCallback(color):
                    def cb(instance, value):
                        newNrOfCards = dict(self.mediator.bidding.nrOfCards)
                        newNrOfCards[color] = value
                        return value >= 0 and sum(newNrOfCards.values()) <= 13

                    return cb

                initialValue = str(
                    self.mediator.bidding.nrOfCards[color]) if color in self.mediator.bidding.nrOfCards else ""
                nrOfCards = buildNumericInput(initialValue, createSetterCallback(color), createValidationCallback(color))
                result.append(nrOfCards)

            return result

        def buildInputNumberOfPoints():
            def setterCallback(instance, value):
                if value != self.mediator.bidding.nrOfPoints:
                    self.mediator.bidding.setNrOfPoints(value)
            
            def validationCallback(instance, value):
                return value >= 0 and value <= 37

            initialValue = str(self.mediator.bidding.nrOfPoints) if self.mediator.bidding.nrOfPoints != None else ''
            nrOfPoints = buildNumericInput(initialValue, setterCallback, validationCallback)

            return nrOfPoints

        questions = BoxLayout(orientation='vertical')
        questions.add_widget(buildText("Hoe ziet uw hand eruit?", size_hint=(1.0, None)))

        gridLyt = GridLayout(cols=2)
        gridLyt.add_widget(buildLabel('Totaal aantal punten'))
        gridLyt.add_widget(buildInputNumberOfPoints())
        for w in buildNumberInSuit():
            gridLyt.add_widget(w)

        questions.add_widget(gridLyt)
        
        return questions

    def build(self):
        self.rootLayout.add_widget(buildMenu(self.mediator, size_hint=(0.2, 0.1)))
        self.rootLayout.add_widget(self.buildQuestions())
        self.rootLayout.add_widget(
            buildButton('Klaar', lambda i: self.mediator.closeSpecification(), size_hint=(1.0, 0.1)))

    def onDisplay(self):
        self.reset()

    def reset(self):
        self.rootLayout.clear_widgets()
        self.build()
