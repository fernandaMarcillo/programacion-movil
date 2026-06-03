from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from admin.admin_data import productos


class ProductScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        self.nombre = TextInput(
            hint_text="Nombre del producto"
        )

        self.precio = TextInput(
            hint_text="Precio"
        )

        btn_agregar = Button(
            text="Agregar Producto"
        )

        btn_agregar.bind(
            on_press=self.agregar_producto
        )

        self.lista = BoxLayout(
            orientation="vertical"
        )

        self.layout.add_widget(self.nombre)
        self.layout.add_widget(self.precio)
        self.layout.add_widget(btn_agregar)
        self.layout.add_widget(self.lista)

        self.add_widget(self.layout)

        self.actualizar_lista()

    def agregar_producto(self, instance):

        if not self.nombre.text or not self.precio.text:
            return

        nuevo = {
            "id": len(productos) + 1,
            "nombre": self.nombre.text,
            "precio": float(self.precio.text)
        }

        productos.append(nuevo)

        self.nombre.text = ""
        self.precio.text = ""

        self.actualizar_lista()

    def eliminar_producto(self, producto):

        productos.remove(producto)

        self.actualizar_lista()

    def actualizar_lista(self):

        self.lista.clear_widgets()

        for producto in productos:

            fila = BoxLayout(size_hint_y=None, height=40)

            texto = Label(
                text=f"{producto['nombre']} - ${producto['precio']}"
            )

            btn_eliminar = Button(
                text="Eliminar",
                size_hint_x=0.3
            )

            btn_eliminar.bind(
                on_press=lambda x, p=producto:
                self.eliminar_producto(p)
            )

            fila.add_widget(texto)
            fila.add_widget(btn_eliminar)

            self.lista.add_widget(fila)