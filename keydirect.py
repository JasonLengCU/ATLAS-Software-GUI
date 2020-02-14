from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

    
def _on_keyboard(instance, key, scancode, codepoint, modifiers):
    print("Keyboard pressed! {}".format(key))



class Demo(App):
    def build(self):
        button = Button(text="Hello")
        return button
   

Window.bind(on_keyboard=_on_keyboard)


Demo().run()
