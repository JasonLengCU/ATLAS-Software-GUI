from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
import cv2
import random
from kivy.core.window import Window


def vidcap():
    capture = cv2.VideoCapture(0)
    # capture = cv2.VideoCapture('udp://192.168.1.10:1234?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000',cv2.CAP_FFMPEG)
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return capture


class GUIWidget(FloatLayout):
    capture = vidcap()
    # initialization of key press check list
    Push = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0]

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
        # Camera 1
        # read in frame
        ret, frame1 = self.capture.read()
        if ret:
            # finds video size for line positioning
            height, width, channels = frame1.shape
            frame1 = cv2.rectangle(frame1, pt1=(75, 75), pt2=(width - 75, height - 75), color=(0, 255, 0), thickness=5)
            # flips frame to correct orientation
            buf1 = cv2.flip(frame1, 0)
            # creates texture to change image
            buft1 = buf1.tostring()
            texture1 = Texture.create(size=(frame1.shape[1], frame1.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buft1, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.ids.img1.texture = texture1
        # Camera 2
        # read in frame
        ret, frame2 = self.capture.read()
        if ret:
            # adds circle to video
            centx = round(width / 2)
            centy = round(height / 2)
            cv2.circle(frame2, center=(centx, centy), radius=50, color=(0, 255, 0), thickness=5)
            # flips frame to correct orientation
            buf2 = cv2.flip(frame2, 0)
            # creates texture to change image
            buft2 = buf2.tostring()
            texture2 = Texture.create(size=(frame2.shape[1], frame2.shape[0]), colorfmt='bgr')
            texture2.blit_buffer(buft2, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.ids.img2.texture = texture2
        cmdout = 'p'
        if sum(self.Push) <= 1:
            # command w
            if self.Push[0]:
                self.ids.L1.col = 1, 0, 0, 1
                cmdout = 'w'
            else:
                self.ids.L1.col = 0, 1, 0, 1
            # command s
            if self.Push[1]:
                self.ids.L4.col = 1, 0, 0, 1
                cmdout = 's'
            else:
                self.ids.L4.col = 0, 1, 0, 1
            # command a
            if self.Push[2]:
                self.ids.L3.col = 1, 0, 0, 1
                cmdout = 'a'
            else:
                self.ids.L3.col = 0, 1, 0, 1
            # command d
            if self.Push[3]:
                self.ids.L2.col = 1, 0, 0, 1
                cmdout = 'd'
            else:
                self.ids.L2.col = 0, 1, 0, 1
            # command h
            if self.Push[4]:
                self.ids.L5top.col = 1, 0, 0, 1
                cmdout = 'h'
            else:
                self.ids.L5top.col = 0, 1, 0, 1
            # command l
            if self.Push[5]:
                self.ids.L6bot.col = 1, 0, 0, 1
                cmdout = 'l'
            else:
                self.ids.L6bot.col = 0, 1, 0, 1
            # command q
            if self.Push[6]:
                self.ids.H2left.col = 1, 0, 0, 1
                cmdout = 'q'
            else:
                self.ids.H2left.col = 0, 1, 0, 1
            # command e
            if self.Push[7]:
                self.ids.H1right.col = 1, 0, 0, 1
                cmdout = 'e'
            else:
                self.ids.H1right.col = 0, 1, 0, 1
            # command n
            if self.Push[8]:
                self.ids.L7top.col = 1, 0, 0, 1
                cmdout = 'n'
            else:
                self.ids.L7top.col = 0, 1, 0, 1
            # command m
            if self.Push[9]:
                self.ids.L8bot.col = 1, 0, 0, 1
                cmdout = 'm'
            else:
                self.ids.L8bot.col = 0, 1, 0, 1
            # command c
            if self.Push[10]:
                self.ids.L9left.col = 1, 0, 0, 1
                cmdout = 'c'
            else:
                self.ids.L9left.col = 0, 1, 0, 1
            # command f
            if self.Push[11]:
                self.ids.L10right.col = 1, 0, 0, 1
                cmdout = 'f'
            else:
                self.ids.L10right.col = 0, 1, 0, 1
        print(cmdout)


class GUIApp(App):
    title = 'Test GUI by Charles'

    def build(self):
        gui = GUIWidget()
        Clock.schedule_interval(gui.update, 1.0/30)
        return gui


if __name__ == '__main__':
    GUIApp().run()