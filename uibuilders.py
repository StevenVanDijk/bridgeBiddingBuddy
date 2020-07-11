from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from enum import Enum

defaultLength = 40
defaultFont = './consola.ttf'

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

kv="""
<RoundedButton@Button>:
    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
    canvas.before:
        Color:
            rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]
"""
class RoundedButton(Button):
    pass

Builder.load_string(kv)

def buildButton(txt, callback):
    btn = Button(color=getColor(txt), text=txt, size_hint=(1.0, None),  height=defaultLength * 2, width=defaultLength * 2, font_name=defaultFont)
    btn.bind(on_press=callback)
    return btn

def buildLabel(txt):
    return Label(color=getColor(txt), text=txt, size_hint=(1.0, None),  height=defaultLength, font_name=defaultFont)
