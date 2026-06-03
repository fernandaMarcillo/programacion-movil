from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from admin.admin_screen import AdminScreen
from admin.product_manager import ProductScreen
from admin.orders_screen import OrdersScreen


class MainApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(
            AdminScreen(name="admin")
        )

        sm.add_widget(
            ProductScreen(name="productos_admin")
        )

        sm.add_widget(
            OrdersScreen(name="pedidos_admin")
        )

        return sm


MainApp().run()