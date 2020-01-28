import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
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

# starts app which calls widget
class CircleApp(App):
    title = 'Limit Switch Design App'
    def build(self):
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




if __name__ == '__main__':  # runs main.py first
    CircleApp().run()

