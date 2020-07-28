import re
from enum import Enum

from kivy.uix.widget import Widget
from kivy import icon_dir
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.core.text import LabelBase
from kivy.core.window import Window

from constants import colors
from mediator import Mediator

fontSize = 20
bigSize = 160
normalSize = 80
smallSize = 40
smallestSize = 20
gap = 6
halfGap = 3
defaultFont = './consola.ttf'
iconFont = './icofont.ttf'
iconTrashcan = u'\uEE09'
iconPencil = u'\uEBF6'

kv = '''
<Widget>:
    font_size: 'fontSizesp'
    font_name: './consola.ttf'
'''.replace('fontSize', str(fontSize))

Builder.load_string(kv)

class ButtonKind(Enum):
    number = 1
    color = 2
    special = 3


def getColor(txt):
    textColor = [1, 1, 1, 1]
    background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if len(txt) <= 2 and ('♣' in txt or '♠' in txt):
        textColor = [0, 0, 0, 1]
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if len(txt) <= 2 and ('♦' in txt or '♥' in txt):
        textColor = [1, 0, 0, 1]
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if len(txt) <= 4 and ('SA' in txt or 'pass' in txt):
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if 'X' == txt:
        background_color = [1, 0, 0, 1]
    if 'XX' == txt:
        background_color = [0, 0, 1, 1]
    if '?' == txt:
        textColor = [0, 0, 0, 1]
        background_color = [1, 1, 0, 1]
    if '1' == txt or '2' == txt or '3' == txt or '4' == txt or '5' == txt or '6' == txt or '7' == txt:
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if 'N' == txt or 'W' == txt or 'E' == txt or 'S' == txt:
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    if 'Undo' == txt:
        background_color = [30 / 256, 130 / 256, 76 / 256, 1]
    return (textColor, background_color)


def buildButton(content, callback, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    widget = Button(size_hint=widgetSizeHint,
                    font_name=defaultFont,
                    padding=(10, 10))
    if isinstance(content, str):
        (col, bcol) = getColor(content)
        widget.text = content
        widget.color = col
        widget.background_normal = ''
        widget.background_color = bcol
    else:
        widget.add_widget(content)
    widget.bind(on_press=callback)
    return widget


def buildIconButton(icon, callback, size_hint=None):
    widget = buildButton(icon, callback, size_hint)
    widget.font_name = iconFont
    return widget


def buildLabel(txt, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    (col, bcol) = getColor(txt)
    return Label(color=col,
                 text=str(txt),
                 size_hint=widgetSizeHint,
                 font_name=defaultFont)


def buildToggle(txt, isDown, callback, group=None, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    state = 'down' if isDown else 'normal'
    (col, bcol) = getColor(txt)
    widget = ToggleButton(group=group,
                          state=state,
                          color=col,
                          background_normal = '',
                          background_color=bcol,
                          text=txt,
                          size_hint=widgetSizeHint,
                          font_name=defaultFont)
    widget.bind(on_press=callback)
    return widget


def buildNumericInput(text, callback, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint

    leftLyt = GridLayout(cols=1, size_hint=widgetSizeHint, padding=[gap]) # contains the numeric input

    class NumInput(TextInput):
        pat = re.compile('[^0-9]')

        def __init__(self, **kwargs):
                super().__init__(**kwargs)

        def insert_text(self, substring, from_undo=False):
            pat = self.pat
            s = re.sub(pat, '', substring)
            return super(NumInput, self).insert_text(s, from_undo=from_undo)

    def plusCallback(i):
        s = widget.text
        if s.isdigit():
            widget.text = str(int(s) + 1)
        else:
            widget.text = str(0)

    def minCallback(i):
        s = widget.text
        if s.isdigit():
            val = int(s)
            if val > 0:
                widget.text = str(val - 1)
        else:
            widget.text = str(0)

    plusBtn = buildButton('+', plusCallback)
    minBtn = buildButton('-', minCallback)
    
    widget = NumInput(text=text, multiline=False, size_hint=(1.0, None))
    widget.height = str(fontSize + widget.padding[0] * 2) + 'sp'
    widget.bind(text=callback)
    widget.halign = 'center'

    leftLyt.add_widget(plusBtn)    
    leftLyt.add_widget(widget)
    leftLyt.add_widget(minBtn)

    return leftLyt


def buildTextInput(callback, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    widget = TextInput(size_hint=widgetSizeHint, multiline=False)
    widget.bind(on_text_validate=callback)

    return widget


def buildText(text, size_hint=None):
    widget = buildLabel(text, size_hint)
    widget.multiline = True
    widget.padding = [20, 20]
    widget.valign = 'top'
    widget.halign = 'left'
    widget.markup = True

    def setTextSize(instance, value):
        widget.text_size = (value, None)

    widget.bind(width=setTextSize)
    return widget

def buildMenu(mediator: Mediator, size_hint=None):
    menuDict = { 'Your hand': lambda: mediator.showSpecification(), 
                 'Biddings': lambda: mediator.showBiddingChooser(),
                 'About BidBud': lambda: mediator.showCredits() }
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    widget = Spinner(text='Menu', size_hint=widgetSizeHint)
    widget.values = list(menuDict.keys())
    widget.bind(text=lambda i, v: menuDict[v]())
    
    def resizeMenu(i, isOpen):
        if isOpen:
            widget.size_hint_x = None
            widget.width = Window.width / 2
        else:
            widget.size_hint = widgetSizeHint
    widget.bind(is_open=resizeMenu)

    return widget