from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from enum import Enum

class BridgeBiddingBuddy(App):
    currentBidding = None
    bidTxt = None
    defaultHeight = 50

    def onAddBid(self, instance):
        self.currentBidding.add_widget(Label(text=instance.text))
        self.bidTxt.focus = True

    def build(self):
        rootLayout = BoxLayout(orientation='horizontal')
        leftLayout = BoxLayout(orientation='vertical')
        rightLayout = BoxLayout(orientation='vertical')

        NOSWlayout = BoxLayout(orientation='horizontal', size_hint=(1.0, None), height=self.defaultHeight)
        for elem in ["N", "E", "S", "W"]:
            NOSWlayout.add_widget(Label(text=elem))

        self.currentBidding = GridLayout(cols=4, size_hint=(1.0, None), height=self.defaultHeight)
        
        leftLayout.add_widget(NOSWlayout)
        leftLayout.add_widget(self.currentBidding)

        self.bidTxt = TextInput(text='', multiline=False)
        self.bidTxt.bind(on_text_validate=lambda instance: self.onAddBid(instance))
        rightLayout.add_widget(self.bidTxt)

        rootLayout.add_widget(leftLayout)
        rootLayout.add_widget(rightLayout)
        return rootLayout

if __name__ == '__main__':
    app = BridgeBiddingBuddy()
    app.run()
        