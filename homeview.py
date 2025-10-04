import flet as ft
from flet import Page, AppBar, Icon, Icons, Text, IconButton, PopupMenuButton, Colors, Column, Container, Card, Row


class VistaAppBar:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Menú principal"
        self.page.window.width = 411
        self.page.window.height = 831
        self.page.window.resizable = False
        self.page.scroll = "auto"
        self.page.clean()

        self.construir_appbar()
        self.construir_contenido()

    def construir_appbar(self):
        self.page.appbar = AppBar(
            leading=IconButton(Icons.HOME, icon_color="white", on_click=lambda e: self.page.go("/home")),
            leading_width=50,
            title=Text("Menú de navegación", color="white", size=20),
            center_title=True,
            bgcolor=Colors.BLUE_GREY,
            actions=[
                PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Login", on_click=lambda e: self.page.go("/login")),
                        ft.PopupMenuItem(text="Soy nuevo", on_click=lambda e: self.page.go("/registro")),
                        ft.PopupMenuItem(text="Home", on_click=lambda e: self.page.go("/home")),
                    ]
                ),
            ],
        )

    def construir_contenido(self):
        mensaje = Text("Prueba mamalona", size=18, weight="bold", color="white")

        tarjeta = Card(
            content=Container(
                content=Column(
                    controls=[
                        mensaje,
                        Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Login",
                                    bgcolor=Colors.BLUE,
                                    color="white",
                                    on_click=lambda e: self.page.go("/login")
                                ),
                                ft.ElevatedButton(
                                    text="Registro",
                                    bgcolor=Colors.GREEN,
                                    color="white",
                                    on_click=lambda e: self.page.go("/registro")
                                ),
                            ],
                            alignment="center",
                            spacing=20
                        )
                    ],
                    spacing=20,
                    alignment="center"
                ),
                padding=30,
                alignment=ft.alignment.center
            )
        )

        self.page.add(
            Column(
                controls=[tarjeta],
                alignment="center",
                horizontal_alignment="center"
            )
        )
