import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock



class Circleswitch(Widget):
    r = NumericProperty
    a = 11
    b = 10
# start circle off as green
    def __init__(s, **kwargs):
        s.r = 0
        s.g = 1
        super(Circleswitch, s).__init__(**kwargs)
    a = 100
    b = 17
    # if the limit switch is on
    if a == b:
        print('a is equal to b')
    # lines 19-22 work to change color to solid red
        # def __init__(s, **kwargs):
           # s.r = 1
           # s.g = 0
           #  super(Circleswitch, s).__init__(**kwargs)
    # lines up until second "elif" are attempt at making ellipse "flash"
    elif a > b:
        print('a is greater than b')
        def __init__(s, **kwargs):
            s.r = 1
            s.g = 0
            super(Circleswitch, s).__init__(**kwargs)
        # if the limit switch is off
    elif a < b:
        print('a is less than b')
        def __init__(s, **kwargs):
            s.r = 0
            s.g = 1
            super(Circleswitch, s).__init__(**kwargs)
# https://stackoverflow.com/questions/57080830/how-to-change-label-background-color-dynamically-in-kivy
class Circles(Widget):
    allcircles = ObjectProperty(None)

    def recolor(self):
        self.allcircles.rgba = (1, 1, 1, 1)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# starts app which calls widget
class CircleApp(App):
    title = 'Limit Switch Design App'
    def build(self):
        return Circleswitch()


if __name__ == '__main__':  # runs main.py first
    CircleApp().run()
