# Archivo: de la appbar para mayor control

import flet as ft
from flet import AppBar, IconButton, Icons, Text, FontWeight, PopupMenuButton, PopupMenuItem

def create_appbar(page: ft.Page):
    """
    Crea y devuelve un objeto AppBar reutilizable.
    Necesita el objeto 'page' para manejar la navegación.
    """
    return AppBar(
        leading=IconButton(Icons.HOME, icon_color="black", on_click=lambda e: page.go("/home")),
        leading_width=50,
        title=Text("BINCO", color="white", size=20, weight=FontWeight.BOLD),
        center_title=True,
        bgcolor="#f8b204",
        actions=[
            PopupMenuButton(
                icon_color="black",
                items=[
                    PopupMenuItem(text="Login", on_click=lambda e: page.go("/login")),
                    PopupMenuItem(text="Soy nuevo", on_click=lambda e: page.go("/registro")),
                    PopupMenuItem(text="Home", on_click=lambda e: page.go("/home")),
                ]
            ),
        ],
    )