from kivy.app import App
from kivy.uix.label import Label
 
class FirstApp(App):
    def build(self):
        
        return Label(text='Utopian bir steemit projesidir.')

FirstApp().run()
