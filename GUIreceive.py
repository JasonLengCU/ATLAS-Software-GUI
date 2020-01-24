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
from datetime import datetime

# Window.fullscreen = 'auto'
open('file.txt', 'w').close()

def ServerBuild():
    # sets up the port to listen for client_cv.py for video stream
    HOST = ''
    PORT = 8089
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')
    Global.conn, Global.addr = s.accept()


def listendata():
    # data listening function
    # currently has an issue with reading garbage after the first frame, potentially caused by send/recieve de-syncing
    # Potential fix: Improved data delimiter; buffer adjustment (cleard, FIFO,etc.)
    packed_msg_size = b''
    while True:
        data = b''
        # Initializes data as type bytes
        payload_size = struct.calcsize("L")
        while len(data) < payload_size:
            data += Global.conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        # Retrieve all data based on message size
        print(msg_size)
        while len(data) < msg_size:
            data += Global.conn.recv(4096)
        # data log gather
        logdata(data)
        frame_data = data[:msg_size]
        # data = data[msg_size:]
        # Extract frame
        frame = pickle.loads(frame_data)
        # display image from cam in opencv window
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        Global.texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        Global.texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')


def logdata(data):
    f = open('datalog.txt', "a")
    f.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), data))
    f.close()


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
        ServerBuild()
        print('b')
        t1 = threading.Thread(target=listendata())
        t1.start()
        Clock.schedule_interval(self.update, 1.0 / 33.0)
        return RootWidget()

    def update(self, dt):
        self.root.ids.img1.texture = Global.texture1
        self.root.ids.img2.texture = Global.texture1


if __name__ == '__main__':
    MainApp().run()
