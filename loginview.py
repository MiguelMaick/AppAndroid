import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, MainAxisAlignment, Card, Container

class VistaLogin:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Login"
        self.page.clean()

        self.txt_user = TextField(label="Usuario", width=300)
        self.txt_password = TextField(label="Contraseña", password=True, width=300)
        self.btn_login = ElevatedButton(text="Iniciar sesión", on_click=self.login, bgcolor=ft.Colors.BLUE, color="white")
        self.lbl_message = Text("Ingresa tus datos", color="blue", size=16)

        card = Card(
            content=Container(
                content=Column(
                    controls=[
                        self.lbl_message,
                        self.txt_user,
                        self.txt_password,
                        self.btn_login
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=20,
                width=350
            )
        )

        self.page.add(
            Column(
                controls=[card],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment="center"
            )
        )

    def login(self, e):
        self.lbl_message.value = f"Bienvenido, {self.txt_user.value}"
        self.lbl_message.color = "green"
        self.page.update()
