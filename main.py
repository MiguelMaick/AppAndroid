import flet as ft
from homeview import VistaAppBar
from loginview import VistaLogin
from registroview import VistaRegistro

def main(page: ft.Page):
    def cambiar_vista(e):
        page.clean()

        if e.route == "/home":
            VistaAppBar(page)
        elif e.route == "/login":
            VistaLogin(page)
        elif e.route == "/registro":
            VistaRegistro(page)

        page.update()

    page.on_route_change = cambiar_vista
    page.go("/home")

ft.app(target=main)