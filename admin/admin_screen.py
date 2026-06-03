from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class AdminScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        titulo = Label(
            text="PANEL ADMINISTRADOR",
            font_size=24,
            size_hint=(1, 0.2)
        )

        btn_productos = Button(
            text="Gestionar Productos"
        )

        btn_pedidos = Button(
            text="Ver Pedidos"
        )

        btn_productos.bind(
            on_press=lambda x: self.ir_productos()
        )

        btn_pedidos.bind(
            on_press=lambda x: self.ir_pedidos()
        )

        layout.add_widget(titulo)
        layout.add_widget(btn_productos)
        layout.add_widget(btn_pedidos)

        self.add_widget(layout)

    def ir_productos(self):
        self.manager.current = "productos_admin"

    def ir_pedidos(self):
        self.manager.current = "pedidos_admin"