import re
from enum import Enum

from kivy import icon_dir
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


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
    if txt == iconTrashcan:
        textColor = [1, 0, 0, 1]
    if txt == iconPencil:
        textColor = [0, 0, 0, 1]
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
    widget = Button(size_hint=widgetSizeHint, padding=(10, 10))
    if isinstance(content, str):
        (col, bcol) = getColor(content)
        widget.text = content
        widget.color = col
        widget.background_normal = ''
        widget.background_color = bcol
    else:
        widget.add_widget(content)
        widget.bind(width=lambda i, value: setattr(content, 'width', value))
        widget.bind(height=lambda i, value: setattr(content, 'height', value))
        widget.bind(pos=lambda i, value: setattr(content, 'pos', value))
    widget.bind(on_press=callback)
    return widget


def buildIconButton(icon, callback, size_hint=None):
    widget = buildButton(icon, callback, size_hint)
    widget.font_name = iconFont
    widget.multiline = True
    return widget


def buildLabel(txt, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    (col, bcol) = getColor(txt)
    return Label(color=col,
                 text=str(txt),
                 size_hint=widgetSizeHint)


def buildToggle(txt, isDown, callback, group=None, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    state = 'down' if isDown else 'normal'
    (col, bcol) = getColor(txt)
    widget = ToggleButton(group=group,
                          state=state,
                          color=col,
                          background_normal='',
                          background_color=bcol,
                          text=txt,
                          size_hint=widgetSizeHint)
    widget.bind(on_press=callback)
    return widget


def buildNumericInput(text, setterCallback, validationCallback, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint

    leftLyt = GridLayout(cols=1, size_hint=widgetSizeHint,
                         padding=[gap])  # contains the numeric input

    class NumInput(TextInput):
        pat = re.compile('[^0-9]')

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def insert_text(self, substring, from_undo=False):
            pat = self.pat
            s = re.sub(pat, '', substring)
            newText = self.text + s
            val = 0 if newText  == '' else int(newText)
            if validationCallback(self, val):
                return super(NumInput, self).insert_text(s, from_undo=from_undo)

    widget = NumInput(text=text, input_type='number', multiline=False, size_hint=(1.0, None))
    widget.height = str(fontSize + widget.padding[0] * 2) + 'sp'

    def plusCallback(i):
        s = widget.text
        if s.isdigit():
            val = 0 if s  == '' else int(s)
            newVal = val + 1
            if validationCallback(widget, newVal):
                widget.text = str(newVal)
        else:
            widget.text = str(0)

    def minCallback(i):
        s = widget.text
        if s.isdigit():
            val = 0 if s  == '' else int(s)
            newVal = val - 1
            if validationCallback(widget, newVal):
                widget.text = str(newVal)
        else:
            widget.text = str(0)

    plusBtn = buildButton('+', plusCallback)
    minBtn = buildButton('-', minCallback)

    def _setterCallback(instance, value):
        intVal = 0 if value == '' else int(value)
        setterCallback(instance, intVal)

    widget.bind(text=_setterCallback)
    widget.halign = 'center'

    leftLyt.add_widget(plusBtn)
    leftLyt.add_widget(widget)
    leftLyt.add_widget(minBtn)

    return leftLyt

def buildTextInput(callback, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    widget = TextInput(size_hint=widgetSizeHint)
    widget.bind(on_text_validate=callback)

    return widget


def buildText(text, size_hint=None):
    widgetSizeHint = (1.0, 1.0) if size_hint == None else size_hint
    widget = ScrollView(size_hint=widgetSizeHint)

    txtView = buildLabel(text, size_hint=(1.0, None))
    txtView.multiline = True
    txtView.padding = [20, 20]
    txtView.valign = 'top'
    txtView.halign = 'left'
    txtView.markup = True

    def setTextSize(instance, value):
        txtView.text_size = (value, None)

    txtView.bind(width=setTextSize)
    txtView.bind(texture_size=lambda i, v: setattr(txtView, 'size', v))

    widget.add_widget(txtView)

    return widget


def buildMenu(mediator: Mediator, size_hint=None):
    menuDict = {
        'Jouw hand': lambda: mediator.showSpecification(),
        'Biedingen': lambda: mediator.showBiddingChooser(),
        'Over BidBud': lambda: mediator.showCredits()
    }
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
