import flet as ft
from homeview import HomeView 
from loginview import VistaLogin
from registroview import VistaRegistro

def main(page: ft.Page):
    # La lógica del enrutador ahora es más clara.
    # El nombre 'cambiar_vista' aquí es un poco confuso con el de Flet, 
    # es mejor llamarlo 'route_change_handler' o algo similar, pero lo mantendré.
    def cambiar_vista(route): # El evento se llama 'route' no 'e'
        page.clean()

        if page.route == "/home":
            HomeView(page) 
        elif page.route == "/login":
            VistaLogin(page)
        elif page.route == "/registro":
            VistaRegistro(page)

        page.update()

    page.on_route_change = cambiar_vista
    page.go("/home")

ft.app(target=main)