DEBUG=1
import os
from kaki.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.dialog import MDDialog

from kivymd.uix.menu import MDDropdownMenu
import math

from bmi import ManagerScreens
# from kivymd.icon_definitions import md_icons
Window.size = (350,600)



 
class BMICalc(App,MDApp):
    
    height = NumericProperty(175)
    weight = NumericProperty(75)
    age = NumericProperty(10)
    height_unit = StringProperty('cm')
    weight_unit = StringProperty('kg')
    
    def menu_callback(self, text_item):
        self.menu.dismiss()
        print(text_item)

    weight_items = [
        {
            "text": "kg",
            "viewclass": "OneLineListItem",
            "on_release": lambda x="kg": menu_callback(x),
        },
        {
            "text": "pounds",
            "viewclass": "OneLineListItem",
            "on_release": lambda x="pounds": menu_callback(x),
        },
    ]
    height_items =[
        {
            "text": "cm",
            "viewclass": "OneLineListItem",
            "on_release": lambda x="cm": self.menu_callback(x),
        },
        {
            "text": "inches",
            "viewclass": "OneLineListItem",
            "on_release": lambda x="inches": self.menu_callback(x),
        }
    ]
        
    

    def drop(self,option,this):
        self.menu = MDDropdownMenu(
            caller=this,
            items=option,
            width_mult=2,
        )
        self.menu.open()


    

    def weight_increase(self):
        self.weight += 1
    def weight_decrease(self):
        self.weight -= 1

    def age_increase(self):
        self.age += 1
    def age_decrease(self):
        self.age -= 1

    def height_increase(self):
        self.height += 1
    def height_decrease(self):
        self.height -= 1

    def calculate_bmi(self):
        bmi = round((self.weight)/((self.height*0.01)**2),1)
        result_popup = MDDialog(title='BMI',text=f"Your BMI is {bmi}",size_hint=[.8,.3])
        result_popup.open()

    DEBUG=1
    
    KV_FILES = {
        os.path.join(os.getcwd(),"bmi.kv")
    }
    CLASSES = {
        "ManagerScreens":"bmi",
        "MyHomeScreen":"bmi",
        "ResultScreen":"bmi",
    }
    AUTORELOADER_PATHS = [(".",{"recursive":True})]
    
    

    
    def build_app(self):
        Window.bind(on_keyboard=self._rebuild)
        self.sm = ManagerScreens()

        # self.home_page = MyHomeScreen()
        # screen = Screen(name='home')
        # screen.add_widget(self.home_page)
        # self.sm.add_widget(screen)

        # self.result_page =ResultScreen()
        # screen = Screen(name='result')
        # screen.add_widget(self.result_page)
        # self.sm.add_widget(screen)

        return self.sm

    def _rebuild(self,*args):
        if args[1] == 32:
            self.rebuild()

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
    BMICalc().run()
    # math-integral-box': '￩'