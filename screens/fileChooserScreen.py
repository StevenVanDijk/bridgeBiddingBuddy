from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from bidding import Bidding
from mediator import Mediator
from uibuilders import (buildButton, buildIconButton, buildLabel,
                        buildMultilineLabel, buildText, buildTextInput, gap,
                        halfGap, iconPencil, iconTrashcan)


class FileChooserScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.mediator = mediator
        self.add_widget(self.rootLayout)
        self.reset()

    def build(self):
        newBidBtn = buildButton('Nieuwe bieding', lambda i: self.mediator.editBidding(Bidding()), size_hint=(1.0, 0.1))

        encloseLyt = BoxLayout(size_hint=(1.0, 0.85))
        scrlView = ScrollView(size_hint=(1.0, None), scroll_type=['content', 'bars'], bar_width='10dp')
        encloseLyt.bind(size=scrlView.setter('size'))
        listLyt = GridLayout(cols=1, spacing=10, size_hint_y=None)
        listLyt.bind(minimum_height=listLyt.setter('height'))
        keys = self.mediator.getBiddingKeys()
        for (key, name, contract) in reversed(keys):  # ensure most recent is at the top

            def createCallbackSelect(key):
                def cb(instance):
                    self.mediator.loadBidding(key)

                return cb

            def createCallbackDelete(key):
                def cb(instance):
                    self.mediator.deleteBidding(key)

                return cb

            def createCallbackEdit(key, name):
                def cb(instance):
                    dad = instance.parent.parent  # GridLayout -> BoxLayout
                    dad.clear_widgets()

                    def setNameCallback(instance):
                        self.mediator.changeBiddingName(key, instance.text)

                    input = buildTextInput(setNameCallback, size_hint=(0.8, 1.0))
                    input.text = name
                    dad.add_widget(input)
                    dad.add_widget(buildButton('Klaar', lambda i: setNameCallback(input), size_hint=(0.2, 1.0)))

                return cb

            itemLyt = BoxLayout(orientation='horizontal', size_hint=(1.0, None))

            btns = GridLayout(rows=1, spacing=[gap, 0], padding=[gap, 0], size_hint=(0.2, 1.0))
            btns.add_widget(buildIconButton(iconPencil, createCallbackEdit(key, name)))
            btns.add_widget(buildIconButton(iconTrashcan, createCallbackDelete(key)))

            itemNameLyt = AnchorLayout()
            itemNameLyt.add_widget(buildMultilineLabel(name))
            itemLyt.add_widget(buildButton(itemNameLyt, createCallbackSelect(key), size_hint=(0.7, 1.0)))
            itemLyt.add_widget(buildText(contract, size_hint=(0.1, 1.0)))
            itemLyt.add_widget(btns)

            newBidBtn.bind(height=itemLyt.setter('height'))

            listLyt.add_widget(itemLyt)

        scrlView.add_widget(listLyt)
        encloseLyt.add_widget(scrlView)
        self.rootLayout.add_widget(encloseLyt)
        self.rootLayout.add_widget(BoxLayout(size_hint=(1.0, 0.05)))
        self.rootLayout.add_widget(newBidBtn)

    def onDisplay(self):
        self.reset()

    def reset(self):
        self.rootLayout.clear_widgets()
        self.build()
