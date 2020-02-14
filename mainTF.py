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

    Push_w = False
    Push_s = False
    Push_a = False
    Push_d = False

    def __init__(self, **kwargs):
        super(GUIWidget, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self, *args):
        if args[1] == 119:
            self.Push_w = False
        if args[1] == 115:
            self.Push_s = False
        if args[1] == 97:
            self.Push_a = False
        if args[1] == 100:
            self.Push_d = False

    def _keydown(self, *args):
        if args[1] == 119:
            self.Push_w = True
        if args[1] == 115:
            self.Push_s = True
        if args[1] == 97:
            self.Push_a = True
        if args[1] == 100:
            self.Push_d = True

    def update(self, dt):
        # Camera 1
        # read in frame
        ret, frame1 = self.capture.read()
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
        if self.Push_w:
            self.ids.L1.col = 1, 0, 0, 1
        else:
            self.ids.L1.col = 0, 1, 0, 1
        if self.Push_s:
            self.ids.L4.col = 1, 0, 0, 1
        else:
            self.ids.L4.col = 0, 1, 0, 1
        if self.Push_a:
            self.ids.L3.col = 1, 0, 0, 1
        else:
            self.ids.L3.col = 0, 1, 0, 1
        if self.Push_d:
            self.ids.L2.col = 1, 0, 0, 1
        else:
            self.ids.L2.col = 0, 1, 0, 1


class GUIApp(App):
    title = 'Test GUI by Charles'

    def build(self):
        gui = GUIWidget()
        Clock.schedule_interval(gui.update, 1.0/30)
        return gui


if __name__ == '__main__':
    GUIApp().run()