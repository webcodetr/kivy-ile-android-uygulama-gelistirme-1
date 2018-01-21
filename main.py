from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
Builder.load_file('main.kv')

sm = ScreenManager()
sm.add_widget(second(name='second'))

class SecondApp(App):

    def build(self):
        return sm 

if __name__ == '__main__':
    SecondApp().run()
