from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from login.login_screen import LoginScreen
from login.register_screen import RegisterScreen
from login.profile_screen import ProfileScreen


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


if __name__ == '__main__':
    AuthApp().run()