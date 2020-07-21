from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class FileChooserScreen(Screen):
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.add_widget(self.rootLayout)
        self.build()

    def build(self):
        pass
