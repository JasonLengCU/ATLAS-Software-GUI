import kivy
kivy.require('1.11.1')
from kivy.app import App
<<<<<<< HEAD
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
=======
>>>>>>> 3f83b988a80fd912faafefbf973a36bb8ff96dd5
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
<<<<<<< HEAD
import itertools
from itertools import cycle
import numpy
from kivy.animation import Animation




Builder.load_string(''' 
#:kivy 1.11.1

<Circleswitch@Widget>:
    col: 0,1,0,1
    canvas.before:
        Color:
            rgba: self.col
        Ellipse:
            pos: (100,100)
            size: self.height/5., self.height/5

<RootWidget>:
    GridLayout:
        id: limitgridone
        rows: 3
        cols: 3
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: root.width, root.height
        GridLayout:
            id: LSpanel
            rows: 1
            cols: 2
            canvas:
                Color:
                    rgba: 0, 0, 0.4, 1
                Rectangle:
                    pos: self.width*1.05, LSpanel.height*.05
                    size: self.width*0.9, self.height*0.9  
            Circleswitch: #creates a brand new object using lightwidget rules
                id: L1
               
                
              

''')

class RootWidget(FloatLayout):
    pass

=======



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
>>>>>>> 3f83b988a80fd912faafefbf973a36bb8ff96dd5
# starts app which calls widget
class CircleApp(App):
    title = 'Limit Switch Design App'
    def build(self):
<<<<<<< HEAD
        Clock.schedule_interval(self.change, .10)
        Clock.schedule_interval(self.turngreen,.23)
        return RootWidget()


    def change(self, dt):
         self.root.ids.L1.col = 1, 0, 0, 1
         #self.root.ids.L1.col = int(cycle(range(1))), 0, 0, 1
         #numberfirst = itertools.cycle([0,1])
         # self.root.ids.L1.col = itertools, 0, 0, 1
    def turngreen(self, dt):
         self.root.ids.L1.col = 0, 1, .3, 1


=======
        return Circleswitch()
>>>>>>> 3f83b988a80fd912faafefbf973a36bb8ff96dd5


if __name__ == '__main__':  # runs main.py first
    CircleApp().run()
<<<<<<< HEAD

=======
>>>>>>> 3f83b988a80fd912faafefbf973a36bb8ff96dd5
