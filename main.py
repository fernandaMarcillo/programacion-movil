from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from login.login_screen import LoginScreen
from admin.admin_screen import AdminScreen
from login.register_screen import RegisterScreen
from admin.product_manager import ProductScreen
from login.profile_screen import ProfileScreen
from admin.orders_screen import OrdersScreen

class AuthApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Pink'
        
        # Crear ScreenManager
        sm = ScreenManager()
        
        # Agregar pantallas
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ProfileScreen(name='profile'))
        
        return sm
        
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
AuthApp().run()
