import flet as ft
from flet import (
    Page, Text, Column, Container, Card, Row, 
    ElevatedButton, FontWeight, alignment
)

# 1. Se cambió el nombre de la clase a algo más descriptivo
class HomeView:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Menú principal"
        self.page.window.width = 411
        self.page.window.height = 831
        self.page.window.resizable = False
        self.page.scroll = "auto"

        self.page.clean()
        
        # 2. Se eliminó la llamada a construir_appbar()
        self.construir_contenido()

    # 3. Se eliminó por completo el método construir_appbar()

    def construir_contenido(self):
        mensaje = Text("BINCO", text_align="center", size=18, weight=FontWeight.BOLD, color="#f8b204")

        tarjeta = Card(
            content=Container(
                content=Column(
                    controls=[
                        mensaje,
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="Login",
                                    bgcolor="#f8b204",
                                    color="black",
                                    on_click=lambda e: self.page.go("/login")
                                ),
                                ElevatedButton(
                                    text="Registro",
                                    bgcolor="#f8b204",
                                    color="black",
                                    on_click=lambda e: self.page.go("/registro")
                                ),
                            ],
                            alignment="center",
                            spacing=20
                        )
                    ],
                    spacing=20,
                    horizontal_alignment="center"
                ),
                padding=30
            )
        )

        # 4. Se usa un Container con 'expand=True' para garantizar el centrado perfecto
        contenedor_centrado = Container(
            content=tarjeta,
            expand=True,
            alignment=alignment.center
        )

        self.page.add(contenedor_centrado)