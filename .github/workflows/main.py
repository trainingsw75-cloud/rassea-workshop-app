from kivy.app import App
from kivy.uix.label import Label

class RasseaWorkshopApp(App):
    def build(self):
        return Label(text='Hello Rassea Workshop!')

if __name__ == '__main__':
    RasseaWorkshopApp().run()
