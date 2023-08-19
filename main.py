from kivy.config import Config
from kivy.graphics import Color, Triangle, Quad
from kivy.uix.button import Button

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
import pywhatkit
import time
import pyautogui
from pynput.keyboard import Key, Controller


class Main_widget(Widget):

    keyboard = Controller()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Wats Auto",pos=(80,500),font_size=50))
        self.add_widget(Label(text="enter number :", pos=(20, 400), font_size=20))
        self.number=TextInput(size=(150,30),pos=(50,380))
        self.add_widget(self.number)
        self.add_widget(Label(text="enter msg :", pos=(10, 300), font_size=20))
        self.msg=TextInput(size=(150,80),pos=(50,250))
        self.add_widget(self.msg)
        self.button=Button(text="send",size=(70,70),pos=(120,50),background_color=(1,0.5,0.5),background_normal=(""),font_size=25)
        self.add_widget(self.button)
        self.button.bind(on_press=self.pressed)
        self.hour=TextInput(size=(30,30),pos=(50,150))
        self.add_widget(self.hour)
        self.add_widget(Label(text="hour :", pos=(20, 160), font_size=18))
        self.minute=TextInput(size=(30,30),pos=(150,150))
        self.add_widget(self.minute)
        self.add_widget(Label(text="minute :", pos=(120, 160), font_size=18))

        with self.canvas.before:
            Color(0.2,0.5,0.4,0.6)
            Quad(points=(0,0,0,600,300,600,300,0))

    def pressed(self,instances):
        self.send_whatsapp_message()

    def send_whatsapp_message(self):
        pywhatkit.sendwhatmsg(
            phone_no=self.number.text,
            message=self.msg.text,
            time_hour=int(self.hour.text),
            time_min=int(self.minute.text)

        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        print("Message sent!")


class Wats_Auto(App):
    def build(self):
        return Main_widget()


Wats_Auto().run()
