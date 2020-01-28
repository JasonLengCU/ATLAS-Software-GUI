from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
import cv2
import random
from kivy.core.window import Window

Builder.load_string('''
<Light@Widget>
    col: 1,0,0,1
    canvas:
        Color:
            rgba: self.col
        Ellipse:
            size: self.width/5, self.width/5
            pos: self.center_x - self.width/10, self.center_y - self.width/10

<RootWidget>
    GridLayout:
        id: gridmain
        rows: 2
        cols: 1
        canvas:
            Color:
                rgba: 0.8, 0.8, 0.8, 1
            Rectangle:
                pos: self.pos
                size: root.width, root.height
        GridLayout:
            id: gridupper
            size_hint_y: 0.5
            rows:1
            cols:2
            Image:
                id: img1
                source: '<random_name>.jpg'
                allow_stretch: False
            Image:
                id: img2
                source: '<random_name>.jpg'
                allow_stretch: False
        GridLayout:
            id: gridlower
            size_hint_y: 0.5
            padding: 10
            rows:1
            cols:3
            Label:
                id: Instruct
                canvas.before:
                    Color:
                        rgba: 0, 0.4, 0, 1
                    Rectangle:
                        pos: self.pos
                        size: self.width, self.height
                text: 'Testing GUI\\nEXTREMELY rough testing\\nenvironment for learning Kivy'
                halign: 'center'
                color: 0,0,0,1
            GridLayout:
                id: LSpanel
                rows: 1
                cols: 1
                canvas:
                    Color:
                        rgba: 0, 0, 0.4, 1
                    Rectangle:
                        pos: self.pos
                        size: self.width, self.height
                Light:
                    id: L1
            FloatLayout:
                id: Panel3
                canvas:
                    Color:
                        rgba: 0.4, 0, 0, 1
                    Rectangle: 
                        pos: self.pos
                        size: self.width, self.height
                AsyncImage:
                    source: 'https://st.depositphotos.com/1902695/4334/i/950/depositphotos_43347351-stock-photo-submarine-control-panel.jpg'
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint_x: 0.9 
''')


class RootWidget(FloatLayout):
    pass


class MainApp(App):
    title = 'Test GUI by Charles'
    # pforward = False

    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        fps = self.capture.get(cv2.CAP_PROP_FPS)
        Clock.schedule_interval(self.update, 1.0/fps)
        return RootWidget()

    # def __init__(self, **kwargs):
    #     super(MainApp, self).__init__(**kwargs)
    #     Window.bind(on_key_up=self._keyup)
    #     Window.bind(on_key_down=self._keydown)
    #
    # def _keyup(self,*args):
    #     if args[1] == 119:
    #         self.pfoward = False
    #
    # def _keydown(self,*args):
    #     if args[1] == 119:
    #         self.pforward = True

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
        self.root.ids.img1.texture = texture1

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
        self.root.ids.img2.texture = texture2

        self.root.ids.L1.col = random.random(), random.random(), random.random(), 1
        # print(self.pforward)


if __name__ == '__main__':
    MainApp().run()