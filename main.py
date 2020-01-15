from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window


class BoxSquare(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class BoxGame(Widget):
    square = ObjectProperty(None)

    PushUp = False
    
    PushDown = False
    
    def __init__(self, **kwargs):
        super(BoxGame, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self,*args):
        if args[1] == 273:
            self.PushUp = False
        if args[1] == 274:
            self.PushDown = False

    def _keydown(self,*args):
        if args[1] == 273:
            self.PushUp = True
        if args[1] == 274:
            self.PushDown = True

    def reset_square(self,vel=(0,0)):
        self.square.center = self.center
        self.square.velocity = vel
        
    def update(self, dt):
        self.square.move()
        if self.PushUp == True:
            self.square.velocity[1] = 1
        if self.PushDown == True:
            self.square.velocity[1] = -1
        if (self.PushDown == False) & (self.PushUp == False):
            self.square.velocity[1] = 0
        if (self.PushDown == True) & (self.PushUp == True):
            self.square.velocity[1] = 0

        if self.square.velocity[1] == 1:
            print("Up")
        if self.square.velocity[1] == -1:
            print("Down")
        if self.square.velocity[1] == 0:
            print("Stop")
            
        
class BoxApp(App):
    def build(self):
        game = BoxGame()
        game.reset_square()
        Clock.schedule_interval(game.update, 1.0 / 60.0)    
        return game

if __name__ == '__main__':
    BoxApp().run()
