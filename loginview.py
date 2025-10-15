import flet as ft
from flet import (
    Page, TextField, ElevatedButton, Text, Column, 
    MainAxisAlignment, Container, alignment
)
from clientes_model import ClientesModel
from components import create_appbar

class VistaLogin:
    def __init__(self, page: Page):
        self.page = page
        self.page.clean()
        self.page.appbar = create_appbar(self.page)
        self.page.title = "Login"
        # La línea page.clean() aquí es redundante, la quito para mayor claridad

        self.modelo = ClientesModel()

        self.txt_email = TextField(label="Email", width=300)
        self.txt_password = TextField(label="Contraseña", password=True, width=300)
        self.btn_login = ElevatedButton(text="Login", on_click=self.login, bgcolor="#f8b204", color="black")
        self.lbl_message = Text("Ingresa tus datos") # El color por defecto es adecuado para un fondo oscuro

        # 1. Se define la columna con su contenido
        formulario = Column(
            controls=[
                self.lbl_message, 
                self.txt_email, 
                self.txt_password, 
                self.btn_login
            ],
            spacing=20,
            # 2. Se añade alineación horizontal para centrar los campos de texto
            horizontal_alignment="center"
        )
        
        # 3. Se envuelve la columna en un Container que se expande y centra todo
        contenedor_centrado = Container(
            content=formulario,
            expand=True,
            alignment=alignment.center
        )

        self.page.add(contenedor_centrado)

    def login(self, e):
        email = self.txt_email.value
        password = self.txt_password.value

        if self.modelo.autenticar_cliente(email, password):
            self.lbl_message.value = f"Bienvenido, {email}"
            self.lbl_message.color = "green"
        else:
            self.lbl_message.value = "Credenciales inválidas"
            self.lbl_message.color = "red"

        self.page.update()