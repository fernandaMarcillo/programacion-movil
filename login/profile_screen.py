from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from login.usuarios_db import obtener_usuario_actual, limpiar_sesion


class ProfileScreen(Screen):
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
        self.titulo = MDLabel(
            text='PERFIL DE USUARIO',
            halign='center',
            font_style='H5',
            theme_text_color='Primary',
            size_hint_y=None,
            height=50
        )
        
        # Mensaje de bienvenida
        self.bienvenida = MDLabel(
            text='',
            halign='center',
            font_style='H6',
            theme_text_color='Secondary',
            size_hint_y=None,
            height=40
        )
        
        # Nombre del usuario
        self.nombre_label = MDLabel(
            text='',
            halign='center',
            font_style='Body1',
            size_hint_y=None,
            height=40
        )
        
        # Correo electrónico
        self.email_label = MDLabel(
            text='',
            halign='center',
            font_style='Body1',
            size_hint_y=None,
            height=40
        )
        
        # Botón Cerrar Sesión
        btn_logout = MDRaisedButton(
            text='Cerrar Sesión',
            size_hint_y=None,
            height=50,
            md_bg_color=(1.0, 0.3, 0.5, 1),
            on_press=self.logout
        )
        
        layout.add_widget(self.titulo)
        layout.add_widget(self.bienvenida)
        layout.add_widget(self.nombre_label)
        layout.add_widget(self.email_label)
        layout.add_widget(btn_logout)
        
        self.add_widget(layout)

    def on_enter(self):
        """Actualiza la información del perfil cuando se entra a la pantalla"""
        usuario = obtener_usuario_actual()
        if usuario:
            self.bienvenida.text = f'¡Bienvenido, {usuario["nombre"]}!'
            self.nombre_label.text = f'Nombre: {usuario["nombre"]}'
            self.email_label.text = f'Correo: {usuario["email"]}'
   
    
    def logout(self, *args):
        """Cierra la sesión y regresa al login"""
        limpiar_sesion()
        self.manager.current = 'login'
