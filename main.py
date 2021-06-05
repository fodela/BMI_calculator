DEBUG=1
import os
from kaki.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window

from kivymd.uix.menu import MDDropdownMenu
import math

from bmi import ManagerScreens
# from kivymd.icon_definitions import md_icons
Window.size = (350,600)



 
class BMICalc(App,MDApp):
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
    # def build(self):
    #     self.sm = ScreenManager()

    #     self.home_page = MyHomeScreen()
    #     screen = Screen(name='home')
    #     screen.add_widget(self.home_page)
    #     self.sm.add_widget(screen)

    #     self.result_page =ResultScreen()
    #     screen = Screen(name='result')
    #     screen.add_widget(self.result_page)
    #     self.sm.add_widget(screen)

    #     return self.sm
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