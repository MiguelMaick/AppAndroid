import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, MainAxisAlignment, Card, Container

class VistaRegistro:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Registro"
        self.page.clean()

        self.lbl_message2 = Text("Ingresa tus datos", color="blue", size=16)
        self.txt_user2 = TextField(label="Usuario", width=300)
        self.txt_Nombre = TextField(label="Nombre", width=300)
        self.txt_apmat = TextField(label="Apellido Materno", width=300)
        self.txt_appat = TextField(label="Apellido Paterno", width=300)
        self.txt_password2 = TextField(label="Contraseña", password=True, width=300)
        self.btn_registro = ElevatedButton(text="Registrar", bgcolor=ft.Colors.GREEN, color="white", on_click=self.registro)

        card = Card(
            content=Container(
                content=Column(
                    controls=[
                        self.lbl_message2,
                        self.txt_user2,
                        self.txt_Nombre,
                        self.txt_apmat,
                        self.txt_appat,
                        self.txt_password2,
                        self.btn_registro
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

    def registro(self, e):
        self.lbl_message2.value = f"Usuario {self.txt_user2.value} registrado correctamente"
        self.lbl_message2.color = "green"
        self.page.update()
