from kivy.app import App
from kivy.uix.label import Label

class DielnaApp(App):
    def build(self):
        return Label(text='Vitaj v dielni!')

if __name__ == '__main__':
    DielnaApp().run()