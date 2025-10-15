import flet as ft
from flet import (
    Page, TextField, ElevatedButton, Text, Column, 
    MainAxisAlignment, Container, alignment  # <-- Se añaden Container y alignment
)
from components import create_appbar

class VistaCatalogo:
    def __init__(self, page: Page):
        self.page = page
        self.page.clean()
        self.page.appbar = create_appbar(self.page)
        self.page.title = "Catálogo"
        # La línea page.clean() aquí es redundante, la quito para mayor claridad

        # Aquí iría la implementación del catálogo
        self.lbl_message = Text("Bienvenido al Catálogo") # El color por defecto es adecuado para un fondo oscuro

        # 1. Se define la columna con su contenido
        formulario = Column(
            controls=[
                self.lbl_message
            ],
            spacing=20,
            # 2. Se añade alineación horizontal para centrar los campos de texto
            horizontal_alignment="center"
        )
        
        # 3. Se envuelve la columna en un Container que se expande y centra todo
        contenedor_centrado = Container(
            content=formulario,
            expand=True,
            alignment=alignment.center
        )

        self.page.add(contenedor_centrado)