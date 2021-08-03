from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from  adaptors.api import getItems
from kivy.metrics import dp


class ItemTable(MDBoxLayout):
    def __init__(self, **kwargs):
        super(ItemTable, self).__init__(**kwargs)
        self.table = MDDataTable(use_pagination=False,
                                 column_data=[
                                 (
                                     "Название", dp(40)
                                 ),
                                 (
                                     "Цена", dp(40)
                                 )])
        self.add_widget(self.table)
        self.init_table()

    def init_table(self):
        self.table.row_data = getItems()


