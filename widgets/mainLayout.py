from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
Builder.load_file("widgets/mainLayout.kv")


class MainLayout(MDBoxLayout):
    orientation = "vertical"