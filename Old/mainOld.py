from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config
import ctypes



user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


Config.set('graphics', 'width', screensize[0])
Config.set('graphics', 'height', screensize[1]-60)

class GUIPanel(Widget):
    pass


class GUIApp(App):

    def build(self):
        return GUIPanel()


if __name__ == '__main__':
    GUIApp().run()