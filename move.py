from kivy.app import App
from kivy.lang import Builder

KV = """

FloatLayout:
    Button:
        text: "hello"
        id: hello
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.3, "right": 0.5}
        on_release:
            world.pos_hint = {"top":0.1, "right": 0.1}
    Button:
        id: world
        text: "world"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.5, "right": 0.9}
        on_release:
            world.pos_hint = {"top":0.9, "right": 0.9}

"""

class MyApp(App):

    def build(self):
        return Builder.load_string(KV)


MyApp().run()