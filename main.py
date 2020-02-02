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
        # Extension 7 Transverse Limits
         self.root.ids.L1.col = 1, 0, 0, 1
         self.root.ids.L2.col = 1, 0, 0, 1
         self.root.ids.L3.col = 1, 0, 0, 1
         self.root.ids.L4.col = 1, 0, 0, 1
        # Vertical Frame Limits
         self.root.ids.L5top.col = 1, 0, 0, 1
         self.root.ids.L6bot.col = 1, 0, 0, 1
        # Back Plate Limits
         self.root.ids.L7top.col = 1, 0, 0, 1
         self.root.ids.L8bot.col = 1, 0, 0, 1
         self.root.ids.L9left.col = 1, 0, 0, 1
         self.root.ids.L10right.col = 1, 0, 0, 1
    def turngreen(self, dt):
        # Extension 7 Transverse Limits
         self.root.ids.L1.col = 0, 1, 0, 1
         self.root.ids.L2.col = 0, 1, 0, 1
         self.root.ids.L3.col = 0, 1, 0, 1
         self.root.ids.L4.col = 0, 1, 0, 1
        # Vertical Frame Limits
         self.root.ids.L5top.col = 0, 1, 0, 1
         self.root.ids.L6bot.col = 0, 1, 0, 1
        # Back Plate Limits
         self.root.ids.L7top.col = 0, 1, 0, 1
         self.root.ids.L8bot.col = 0, 1, 0, 1
         self.root.ids.L9left.col = 0, 1, 0, 1
         self.root.ids.L10right.col = 0, 1, 0, 1


if __name__ == '__main__':  # runs main.py first
    CircleApp().run()

