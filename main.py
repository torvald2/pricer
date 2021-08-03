import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from widgets.create_item import CreateItem


class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(CreateItem(name="item"))



        return self.sm

if __name__ == '__main__':
    MainApp().run()