from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from mediator import Mediator
from kivy.uix.filechooser import FileChooser, FileChooserIconLayout

class FileChooserScreen(Screen):
    mediator: Mediator
    rootLayout = BoxLayout(orientation='vertical')

    def __init__(self, mediator, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.add_widget(self.rootLayout)
        self.build()

    def build(self):
        filechooser = FileChooser()
        filechooser.add_widget(FileChooserIconLayout())
        self.rootLayout.add_widget(filechooser)

    def onDisplay(self):
        pass
