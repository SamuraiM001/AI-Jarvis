from kivy.lang import Builder
from random import randint
import kivy
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch

from kivy.uix.boxlayout import BoxLayout
import pcversion as ai


App.clearcolor = (randint(0,255)/255,randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
App.title = "AI"



class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="Always Play Without Pressing Button?")

    def btn_pressed(self,*args):
        print(self.s.value)
        pt = self.s.value
        print(pt)
        ai.currentrate = self.s.value
        print(ai.currentrate)
        ai.activate()

    def alwaysmode(self,*args):
        if self.switch.active:
            ai.alwayson = True
        else:
            ai.alwayson = False
        
    def build(self):
        b = BoxLayout(orientation = 'vertical')
        btn =Button(text="Activate The AI",pos_hint= {'x': 0, 'y': 1})
        lbl = Label(text="Which Speed Do You  Want It To Speak?")
        self.s = Slider(value_track=True,value_track_color=[0.3, 0, 0.8,1],max =ai.maxrate,min=ai.minrate,value=180)
        self.switch = Switch()
        self.switch.bind(active=self.alwaysmode)
        btn.bind(on_press=self.btn_pressed)
        b.add_widget(self.label)
        b.add_widget(self.switch)
        b.add_widget(lbl)
        b.add_widget(self.s)
        b.add_widget(btn)
        
        return b
    
    
    
if __name__ == '__main__':
    MyApp().run()

