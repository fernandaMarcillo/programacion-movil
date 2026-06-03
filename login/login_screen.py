from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from login.usuarios_db import verificar_credenciales, establecer_usuario_actual


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal
        layout = MDBoxLayout(
            orientation='vertical',
            spacing=20,
            padding=30,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),
            md_bg_color=(1.0, 0.85, 0.9, 1)
        )
        
        # Título
        titulo = MDLabel(
            text='INICIAR SESIÓN',
            halign='center',
            font_style='H5',
            theme_text_color='Primary',
            size_hint_y=None,
            height=50
        )
        
        # Campo de correo/usuario
        self.email_field = MDTextField(
            hint_text='Correo electrónico o usuario',
            helper_text='Ingrese su correo o usuario',
            helper_text_mode='on_focus',
            size_hint_y=None,
            height=50
        )
        
        # Campo de contraseña
        self.password_field = MDTextField(
            hint_text='Contraseña',
            helper_text='Ingrese su contraseña',
            helper_text_mode='on_focus',
            password=True,
            size_hint_y=None,
            height=50
        )
        
        # Mensaje de error
        self.error_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Error',
            size_hint_y=None,
            height=30
        )
        
        # Botón Iniciar Sesión
        btn_login = MDRaisedButton(
            text='Iniciar Sesión',
            size_hint_y=None,
            height=50,
            md_bg_color=(1.0, 0.4, 0.7, 1),
            on_press=self.login
        )
        
        # Botón Ir a Registro
        btn_register = MDRaisedButton(
            text='Ir a Registro',
            size_hint_y=None,
            height=50,
            md_bg_color=(0.8, 0.5, 0.6, 1),
            on_press=self.go_to_register
        )
        
        layout.add_widget(titulo)
        layout.add_widget(self.email_field)
        layout.add_widget(self.password_field)
        layout.add_widget(self.error_label)
        layout.add_widget(btn_login)
        layout.add_widget(btn_register)
        
        self.add_widget(layout)
    
    def login(self, *args):
        email = self.email_field.text.strip()
        password = self.password_field.text.strip()
        
        # Validar campos vacíos
        if not email or not password:
            self.error_label.text = 'Por favor complete todos los campos'
            return
        
        # Validar credenciales
        usuario = verificar_credenciales(email, password)
        
        if usuario:
            establecer_usuario_actual(usuario)
            self.error_label.text = ''
            self.manager.current = 'profile'
        else:
            self.error_label.text = 'Credenciales incorrectas'
    
    def go_to_register(self, *args):
        self.error_label.text = ''
        self.email_field.text = ''
        self.password_field.text = ''
        self.manager.current = 'register'
