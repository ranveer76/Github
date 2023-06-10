import kivy
import pyautogui as p
from time import sleep
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.uix.button import Button


class MainApp(GridLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text='no. of times you want to send'))
        self.a = TextInput()
        self.add_widget(self.a)

        self.add_widget(Label(text='message'))
        self.b = TextInput()
        self.add_widget(self.b)

        self.press = Button(text='run', on_press=self.run)
        self.add_widget(self.press)

    def run(self, instance):
        a1 = self.a.text
        a1 = int(a1)
        b2 = self.b.text
        sleep(3)
        for i in range(a1):
            p.typewrite(b2)
            p.press('enter')


class run_app(App):
    def build(self):
        return MainApp()


if __name__ == '__main__':
    run_app().run()
