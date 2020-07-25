from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from bidding import Bidding
from mediator import Mediator
from uibuilders import buildButton, buildIconButton, buildLabel, iconTrashcan


class FileChooserScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.mediator = mediator
        self.add_widget(self.rootLayout)
        self.reset()

    def build(self):
        newBidBtn = buildButton('New bidding', lambda i: self.mediator.editBidding(Bidding()), size_hint=(1.0, 0.1))

        encloseLyt = BoxLayout(size_hint=(1.0, 0.85))
        scrlView = ScrollView(size_hint=(1.0, None), scroll_type=['content', 'bars'], bar_width='10dp')
        encloseLyt.bind(size=scrlView.setter('size'))
        listLyt = GridLayout(cols=1, spacing=10, size_hint_y=None)
        listLyt.bind(minimum_height=listLyt.setter('height'))
        keys = self.mediator.storage.keys()
        for key in reversed(keys):  # ensure most recent is at the top

            def createcallbackSelect(key):
                def cb(instance):
                    self.mediator.loadBidding(key)

                return cb

            def createcallbackDelete(key):
                def cb(instance):
                    self.mediator.deleteBidding(key)
                
                return cb

            itemLyt = BoxLayout(orientation='horizontal', size_hint=(1.0, None))
            itemLyt.add_widget(buildButton(key, createcallbackSelect(key), size_hint=(0.9, 1.0)))
            itemLyt.add_widget(buildIconButton(iconTrashcan, createcallbackDelete(key), size_hint=(0.1, 1.0)))
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
