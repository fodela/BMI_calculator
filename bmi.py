from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
import math
# from kivymd.icon_definitions import md_icons

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
class ResultScreen(Screen):
    pass


 
class BMI(MDApp):
    def __init__(self):
        Window.size = (350,600)
        super().__init__()
        # options = [{"text":f"opt{i}"}for i in range(5)]   
        # self.dropdown = MDDropdownMenu(
        #     caller = self.MyHomeScreen.ids.drop_item,
        #     items=options,
        #     width_mult=4,
        # )
    def build(self):
        self.sm = ScreenManager()

        self.home_page = MyHomeScreen()
        screen = Screen(name='home')
        screen.add_widget(self.home_page)
        self.sm.add_widget(screen)

        self.result_page =ResultScreen()
        screen = Screen(name='result')
        screen.add_widget(self.result_page)
        self.sm.add_widget(screen)

        return self.sm

    def change_screen(self,screen_name):
        self.sm.current = screen_name

        
    def go_home(self):
        sm = ScreenManager()
        sm.add_widget(MyHomeScreen(name='home'))
        sm.add_widget(ResultScreen(name='result'))
        sm.current = 'home'
    def donothing(self):
        pass

if __name__ == "__main__":
    BMI().run()
    # math-integral-box': '￩'