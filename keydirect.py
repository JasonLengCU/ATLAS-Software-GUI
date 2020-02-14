from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import socket


def conn():
    host = "localhost"
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))
        print('Port Bound')
    except socket.error as e:
        print(str(e))
    return s


class GUIWidget(Button):
    Push = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s = conn()

    def __init__(self, **kwargs):
        super(GUIWidget, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self, *args):
        if args[1] == 119:
            self.Push[0] = False
        if args[1] == 115:
            self.Push[1] = False
        if args[1] == 97:
            self.Push[2] = False
        if args[1] == 100:
            self.Push[3] = False
        if args[1] == 104:
            self.Push[4] = False
        if args[1] == 108:
            self.Push[5] = False
        if args[1] == 113:
            self.Push[6] = False
        if args[1] == 101:
            self.Push[7] = False
        if args[1] == 110:
            self.Push[8] = False
        if args[1] == 109:
            self.Push[9] = False
        if args[1] == 99:
            self.Push[10] = False
        if args[1] == 102:
            self.Push[11] = False

    def _keydown(self, *args):
        if args[1] == 119:
            self.Push[0] = True
        if args[1] == 115:
            self.Push[1] = True
        if args[1] == 97:
            self.Push[2] = True
        if args[1] == 100:
            self.Push[3] = True
        if args[1] == 104:
            self.Push[4] = True
        if args[1] == 108:
            self.Push[5] = True
        if args[1] == 113:
            self.Push[6] = True
        if args[1] == 101:
            self.Push[7] = True
        if args[1] == 110:
            self.Push[8] = True
        if args[1] == 109:
            self.Push[9] = True
        if args[1] == 99:
            self.Push[10] = True
        if args[1] == 102:
            self.Push[11] = True

    def update(self, dt):
        cmdout = 'p'
        if sum(self.Push) <= 1:
            # command w
            if self.Push[0]:
                cmdout = 'w'
            # command s
            if self.Push[1]:
                cmdout = 's'
            # command a
            if self.Push[2]:
                cmdout = 'a'
            # command d
            if self.Push[3]:
                cmdout = 'd'
            # command h
            if self.Push[4]:
                cmdout = 'h'
            # command l
            if self.Push[5]:
                cmdout = 'l'
            # command q
            if self.Push[6]:
                cmdout = 'q'
            # command e
            if self.Push[7]:
                cmdout = 'e'
            # command n
            if self.Push[8]:
                cmdout = 'n'
            # command m
            if self.Push[9]:
                cmdout = 'm'
            # command c
            if self.Push[10]:
                cmdout = 'c'
            # command f
            if self.Push[11]:
                cmdout = 'f'
        print(cmdout)
        self.s.sendto(cmdout.encode('utf-8'), ("127.0.0.1", 5555))


class Direct(App):
    def build(self):
        disp = GUIWidget()
        Clock.schedule_interval(disp.update, 1.0 / 30)
        return disp


if __name__ == '__main__':
    Direct().run()
