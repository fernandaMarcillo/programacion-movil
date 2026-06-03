from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from admin.admin_data import pedidos


class OrdersScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        titulo = Label(
            text="PEDIDOS REALIZADOS",
            font_size=22,
            size_hint=(1, 0.2)
        )

        self.layout.add_widget(titulo)

        for pedido in pedidos:

            texto = Label(
                text=f"{pedido['cliente']} | {pedido['producto']} | ${pedido['total']}"
            )

            self.layout.add_widget(texto)

        self.add_widget(self.layout)