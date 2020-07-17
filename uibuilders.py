from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
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
    background_color = [30,130,76,1]
    if '♣' in txt or '♠' in txt:
        textColor = [0,0,0,1]
        background_color = [30 / 256,130 / 256,76 / 256,1]
    if '♦' in txt or '♥' in txt:
        textColor = [1,0,0,1]
        background_color = [30 / 256,130 / 256,76 / 256,1]
    if 'SA' in txt or 'pass' in txt:
        background_color = [30 / 256,130 / 256,76 / 256,1]
    if 'X' == txt:
        background_color = [1,0,0,1]
    if 'XX' in txt:
        background_color = [0,0,1,1]
    if '?' in txt:
        background_color = [1,1,0,1]
    if '1' in txt or '2' in txt or '3' in txt or '4' in txt or '5' in txt or '6' in txt or '7' in txt:
        background_color = [30 / 256,130 / 256,76 / 256,1]
    if 'N' in txt or 'W' in txt or 'E' in txt or 'S' in txt:
        background_color = [30 / 256,130 / 256,76 / 256,1]
    if 'Undo' in txt:
        background_color = [30 / 256,130 / 256,76 / 256,1]
    return (textColor, background_color)

kv="""
<RoundedButton@Button>:
    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
    canvas.before:
        Color:
            rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [50,]
"""


class RoundedButton(Button):
    pass

Builder.load_string(kv)

def buildButton(txt, callback):
    (col, bcol) = getColor(txt)
    if (txt in ['1', '2', '3', '4', '5', '6', '7', '♦', '♥', '♣', '♠', 'pass', '?', 'X', 'XX', 'SA']) :
        btn = RoundedButton(color=col, text=txt, font_name=defaultFont, background_normal='', background_color=bcol, padding=(10,10))
    else :
        btn = RoundedButton(color=col, text=txt, size_hint=(1.0, None),  height=defaultLength * 2, width=defaultLength * 2, font_name=defaultFont, background_normal='', background_color=bcol)
    btn.bind(on_press=callback)
    # anchorLayout = AnchorLayout(padding=[3], anchor_x="center", anchor_y="center")
    # anchorLayout.add_widget(btn)
    return btn

def buildLabel(txt):
    (col, bcol) = getColor(txt)
    return Label(color=col, text=txt, size_hint=(1.0, None),  height=defaultLength, font_name=defaultFont)
