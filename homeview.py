import flet as ft
from flet import (
    Page, Text, Column, Container, Card, Row,
    ElevatedButton, FontWeight, alignment
)
from pathlib import Path
import traceback
import sys

class HomeView:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Menú principal"
        self.page.window.width = 431
        self.page.window.height = 682
        self.page.window.resizable = False
        self.page.scroll = "auto"

        # Construye contenido protegido
        self.construir_contenido()

    def construir_contenido(self):
        try:
            mensaje = Text("BIENVENIDO A", text_align="center", size=18, weight=FontWeight.BOLD, color="#ffffff")

            imagen = ft.Image(
                src="assets/logo.png", 
                width=150,            
                height=50,
                fit=ft.ImageFit.CONTAIN,
                tooltip="Logo de BINCO"
            )

            tarjeta = Card(
                content=Container(
                    content=Column(
                        controls=[
                            mensaje,
                            imagen,
                            Row(
                                controls=[
                                    ElevatedButton(
                                        text="INICIAR SESIÓN",
                                        bgcolor="#f8b204",
                                        color="black",
                                        on_click=lambda e: self.page.go("/login")
                                    ),
                                    ElevatedButton(
                                        text="CREAR CUENTA",
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

            contenedor_centrado = Container(
                content=tarjeta,
                expand=True,
                alignment=alignment.center
            )

            # Añade al page
            self.page.add(contenedor_centrado)

            # Forzar actualización (en caso de que no se refresque automáticamente)
            self.page.update()

        except Exception as exc:
            # Captura cualquier excepción y la muestra en consola para que no quede negro sin pista
            print("Excepción al construir la UI:", file=sys.stderr)
            traceback.print_exc()
            # Opcional: muestra un mensaje visible en la UI en vez de pantalla negra
            self.page.controls.clear()
            self.page.add(Text("Ocurrió un error al cargar la interfaz. Revisa la consola.", color="red"))
            self.page.update()
