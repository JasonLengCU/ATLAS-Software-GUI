import pickle
import socket
import struct
import threading
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
import cv2
# Global file
import Global
from kivy.core.window import Window
# Window.fullscreen = 'auto'


def serverbuild():
    HOST = ''
    PORT = 8089
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')
    Global.conn, Global.addr = s.accept()


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
            source: 'standin.png'
            allow_stretch: True
        Label:
            text: "I don't suffer from insanity, I enjoy every minute of it. This text is a placeholder"
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Image:
            id: img2
            source: 'standin.png'
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
        print('a')
        serverbuild()
        print('b')
        Clock.schedule_interval(self.update, 1.0 / 33.0)
        return RootWidget()

    def update(self, dt):
        data = b''  ### CHANGED
        payload_size = struct.calcsize("L")
        while len(data) < payload_size:
            data += Global.conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        # Retrieve all data based on message size
        print(msg_size)
        print('a')
        if msg_size <10000000:
            print('b')
            while len(data) < msg_size:
                data += Global.conn.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            # Extract frame
            frame = pickle.loads(frame_data)
            # display image from cam in opencv window
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