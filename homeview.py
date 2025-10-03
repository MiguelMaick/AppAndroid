import flet as ft
from flet import Page, AppBar, Icon, Icons, Text, IconButton, PopupMenuButton, PopupMenuItem, CupertinoFilledButton, Column, Colors

class VistaAppBar:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "AppBar Example"
        self.page.window.width = 411
        self.page.window.height = 831
        self.page.window.resizable = False
        self.page.scroll = "auto"
        self.page.clean()

        self.construir_appbar()
        self.construir_contenido()

    def construir_appbar(self):
        self.page.appbar = AppBar(
            leading=Icon(Icons.HOME, color="white"),
            leading_width=50,
            title=Text("Menú de navegación", color ="white", size = 20),
            center_title=True,
            bgcolor=Colors.BLUE_GREY,
            actions=[
                IconButton(Icons.ANDROID, icon_color = "white"),
                IconButton(Icons.CLOUD, icon_color= "white"),
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
        mensaje = Text("Bienvenido a Python una app bien Perrona!!!")
        boton = CupertinoFilledButton(
            content=Text("Botón de ejemplo"),
            opacity_on_click=0.3,
            on_click=self.boton_click
        )
        

        self.page.add(Column(controls=[mensaje, boton], spacing=20))

    def boton_click(self, e):
        print("Botón en accionamiento")

