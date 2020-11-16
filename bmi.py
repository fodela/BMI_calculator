from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.dialog import MDDialog
import math

class MyHomeScreen(Screen):
    user_height = NumericProperty(175)
    weight = NumericProperty(75)
    
    age = NumericProperty(10)

    def weight_increase(self):
        self.weight += 1
    def weight_decrease(self):
        self.weight -= 1

    def age_increase(self):
        self.age += 1
    def age_decrease(self):
        self.age -= 1

    def user_height_increase(self):
        self.user_height += 1
    def user_height_decrease(self):
        self.user_height -= 1

    def calculate_bmi(self):
        bmi = round((self.weight)/((self.user_height*0.01)**2),1)
        result_popup = MDDialog(title='BMI',text=f"Your BMI is {bmi}",size_hint=[.8,.3])
        result_popup.open()


class BMI(MDApp):
    def __init__(self):
        Window.size = (350,600)
        super().__init__()
        
    

if __name__ == "__main__":
    BMI().run()