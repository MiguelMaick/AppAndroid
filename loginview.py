import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, MainAxisAlignment

class VistaLogin:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Login"
        self.page.clean()

        self.txt_user = TextField(label="Usuario", width=300)
        self.txt_password = TextField(label="Contraseña", password=True, width=300)
        self.btn_login = ElevatedButton(text="Login", on_click=self.login)
        self.lbl_message = Text("Ingresa tus datos", color="blue")

        self.page.add(
            Column(
                controls=[self.lbl_message, self.txt_user, self.txt_password, self.btn_login],
                alignment=MainAxisAlignment.CENTER,
                spacing=20
            )
        )

    def login(self, e):
        self.lbl_message.value = f"Bienvenido, {self.txt_user.value}"
        self.lbl_message.color = "green"
        self.page.update()

