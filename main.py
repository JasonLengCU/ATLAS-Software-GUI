from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
import cv2
from kivy.core.window import Window
Window.fullscreen = 'auto'

Builder.load_string('''
<GridLayout>
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            pos: self.pos
            size: self.size


<RootWidget>
    GridLayout:
        id: gridmain
        # size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:2
        cols:3
        Image:
            id: img1
            source: '<random_name>.jpg'
            allow_stretch: True
        Label:
            text: "I don't suffer from insanity, I enjoy every minute of it. This text is a placeholder"
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Image:
            id: img2
            source: '<random_name>.jpg'
            allow_stretch: True
        AsyncImage:
            source: 'https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg'
        AsyncImage:
            source: 'https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg'
        AsyncImage:
            source: 'https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg'
''')

class RootWidget(FloatLayout):
    pass

class VideoFeed(Widget):
    pass

class MainApp(App):

    def build(self):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return RootWidget()

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.root.ids.img1.texture = texture1
        self.root.ids.img2.texture = texture1

if __name__ == '__main__':
    MainApp().run()