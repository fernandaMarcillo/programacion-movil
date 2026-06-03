from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from login.usuarios_db import guardar_usuario, email_existe
import re


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal
        layout = MDBoxLayout(
            orientation='vertical',
            spacing=15,
            padding=20,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),
            md_bg_color=(1.0, 0.85, 0.9, 1)
        )
        
        # Título
        titulo = MDLabel(
            text='REGISTRO',
            halign='center',
            font_style='H5',
            theme_text_color='Primary',
            size_hint_y=None,
            height=50
        )
        
        # Campo nombre completo
        self.nombre_field = MDTextField(
            hint_text='Nombre completo',
            helper_text='Ingrese su nombre completo',
            helper_text_mode='on_focus',
            size_hint_y=None,
            height=50
        )
        
        # Campo correo electrónico
        self.email_field = MDTextField(
            hint_text='Correo electrónico',
            helper_text='Ingrese su correo electrónico',
            helper_text_mode='on_focus',
            size_hint_y=None,
            height=50
        )
        
        # Campo contraseña
        self.password_field = MDTextField(
            hint_text='Contraseña',
            helper_text='Mínimo 6 caracteres',
            helper_text_mode='on_focus',
            password=True,
            size_hint_y=None,
            height=50
        )
        
        # Campo confirmar contraseña
        self.confirm_password_field = MDTextField(
            hint_text='Confirmar contraseña',
            helper_text='Repita su contraseña',
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
        
        # Botón Registrarse
        btn_register = MDRaisedButton(
            text='Registrarse',
            size_hint_y=None,
            height=50,
            md_bg_color=(1.0, 0.4, 0.7, 1),
            on_press=self.register
        )
        
        # Botón Volver al Login
        btn_back = MDRaisedButton(
            text='Volver al Login',
            size_hint_y=None,
            height=50,
            md_bg_color=(0.8, 0.5, 0.6, 1),
            on_press=self.go_to_login
        )
        
        layout.add_widget(titulo)
        layout.add_widget(self.nombre_field)
        layout.add_widget(self.email_field)
        layout.add_widget(self.password_field)
        layout.add_widget(self.confirm_password_field)
        layout.add_widget(self.error_label)
        layout.add_widget(btn_register)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)
    
    def validar_email(self, email):
        """Valida el formato de email con regex"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def register(self, *args):
        nombre = self.nombre_field.text.strip()
        email = self.email_field.text.strip()
        password = self.password_field.text.strip()
        confirm_password = self.confirm_password_field.text.strip()
        
        # Validar campos vacíos
        if not nombre or not email or not password or not confirm_password:
            self.error_label.text = 'Por favor complete todos los campos'
            return
        
        # Validar formato de email
        if not self.validar_email(email):
            self.error_label.text = 'Formato de correo inválido'
            return
        
        # Validar longitud de contraseña
        if len(password) < 6:
            self.error_label.text = 'La contraseña debe tener al menos 6 caracteres'
            return
        
        # Validar que las contraseñas coincidan
        if password != confirm_password:
            self.error_label.text = 'Las contraseñas no coinciden'
            return
        
        # Validar que el email no esté registrado
        if email_existe(email):
            self.error_label.text = 'Este correo ya está registrado'
            return
        
        # Guardar usuario en memoria
        guardar_usuario(nombre, email, password)
        
        self.error_label.text = ''
        self.nombre_field.text = ''
        self.email_field.text = ''
        self.password_field.text = ''
        self.confirm_password_field.text = ''
        
        # Ir al login
        self.manager.current = 'login'
    
    def go_to_login(self, *args):
        self.error_label.text = ''
        self.nombre_field.text = ''
        self.email_field.text = ''
        self.password_field.text = ''
        self.confirm_password_field.text = ''
        self.manager.current = 'login'
