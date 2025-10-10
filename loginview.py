import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, MainAxisAlignment
from clientes_model import ClientesModel

class VistaLogin:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Login"
        self.page.clean()

        self.modelo = ClientesModel()

        self.txt_email = TextField(label="Email", width=300)
        self.txt_password = TextField(label="Contraseña", password=True, width=300)
        self.btn_login = ElevatedButton(text="Login", on_click=self.login)
        self.lbl_message = Text("Ingresa tus datos", color="blue")

        self.page.add(
            Column(
                controls=[self.lbl_message, self.txt_email, self.txt_password, self.btn_login],
                alignment=MainAxisAlignment.CENTER,
                spacing=20
            )
        )

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