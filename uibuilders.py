from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton  import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from enum import Enum
import re

font_size = 12
bigSize = 160
normalSize = 80
smallSize = 40
smallestSize = 20
defaultFont = './consola.ttf'
colors = ['♣', '♠', '♦', '♥']

class ButtonKind(Enum):
    number = 1
    color = 2
    special = 3

def getColor(txt):
    textColor = [0,1,0,1] 
    if '♣' in txt or '♠' in txt:
        textColor = [0,0,0,1]
    if '♦' in txt or '♥' in txt:
        textColor = [1,0,0,1]
    return textColor

def buildButton(txt, callback, size=None):
    widgetSize = normalSize if size == None else size
    widget = Button(
        color=getColor(txt), 
        text=txt, 
        size_hint=(1.0, None),  
        height=widgetSize, 
        font_name=defaultFont)
    widget.bind(on_press=callback)
    return widget

def buildLabel(txt, size=None, size_hint=None):
    widgetSize = normalSize if size == None else size
    widgetSizeHint = (1.0, None) if size_hint == None else size_hint
    return Label(
        color=getColor(txt), 
        text=txt, 
        size_hint=widgetSizeHint,  
        height=widgetSize, 
        font_name=defaultFont)

def buildToggle(txt, isDown, callback, group=None, size=None):
    state = 'down' if isDown else 'normal'
    widgetSize = normalSize if size == None else size
    widget = ToggleButton(
        group=group, 
        state=state, 
        color=getColor(txt), 
        text=txt, 
        size_hint=(1.0, None),  
        height=widgetSize, 
        font_name=defaultFont)
    widget.bind(on_press=callback)
    return widget

def buildNumericInput(callback, size=None):
    class NumInput(TextInput):
        pat = re.compile('[^0-9]')
        def insert_text(self, substring, from_undo=False):
            pat = self.pat
            s = re.sub(pat, '', substring)
            return super(NumInput, self).insert_text(s, from_undo=from_undo)
    
    widgetSize = normalSize if size == None else size
    widget = NumInput(
        size_hint=(1.0, None),  
        height=widgetSize        
    )
    return widget