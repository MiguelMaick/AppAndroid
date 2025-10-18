import sys
import traceback
import flet as ft
from flet import (
    Page, Text, Container, Column, FontWeight, alignment, MainAxisAlignment,
    Row, Image, BorderRadius, ElevatedButton
)
from components import create_appbar


class VistaCatalogo:
    def __init__(self, page: Page):
        self.page = page
        self.page.clean()
        self.page.bgcolor = "#383838"
        self.page.appbar = create_appbar(self.page)
        self.page.title = "Catálogo"
        self.catalogo()

    def catalogo(self):
        try:
            # Imagen superior
            imagen = ft.Image(
                src="assets/envio.png",
                fit=ft.ImageFit.COVER,
                expand=True,
                height=150,
            )

            # Texto de Categorías
            categorias = Container(
                content=Text(
                    "Categorías",
                    size=22,
                    weight=FontWeight.BOLD,
                    color="white",
                ),
                alignment=alignment.center_left,
                padding=ft.padding.only(left=20, top=10, bottom=10),
                width=self.page.width,
            )

            # Función auxiliar para crear imagen circular con texto
            def imagen_categoria(src, texto):
                return Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            content=Image(
                                src=src,
                                width=90,
                                height=90,
                                fit=ft.ImageFit.COVER,
                            ),
                            width=90,
                            height=90,
                            border_radius=BorderRadius(
                                top_left=45, top_right=45, bottom_left=45, bottom_right=45
                            ),
                            bgcolor="white",
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        ),
                        Text(texto, color="white", size=16, weight=FontWeight.BOLD),
                    ],
                )
            #  Contenedor de categorías
            categorias_imagenes = Row(
                alignment=MainAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    imagen_categoria("assets/anime.jpg", "Anime"),
                    imagen_categoria("assets/musica.jpg", "Música"),
                    imagen_categoria("assets/series.jpg", "Series"),
                ],
            )
            # Contenedor de categorías
            categorias_container = Container(
                content=categorias_imagenes,
                alignment=alignment.center,
                padding=ft.padding.symmetric(vertical=20),
            )

            # Función auxiliar para crear productos (imagen, nombre, precio, botón)
            # es como una plantilla que jala los datos y los acomoda
            def producto(src, nombre, precio):
                return Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        Container(
                            content=Image(
                                src=src,
                                width=100,
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            width=100,
                            height=100,
                            border_radius=BorderRadius(
                                top_left=15, top_right=15, bottom_left=15, bottom_right=15
                            ),
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        ),
                        Text(nombre, color="white", size=14, weight=FontWeight.BOLD),
                        Text(f"${precio} MXN", color="white", size=12),
                        ElevatedButton(
                            text="Agregar",
                            bgcolor="#f8b204",
                            color="black",
                            width=100,
                            height=30,
                            on_click=lambda e: print(f"{nombre} agregado al carrito")
                        ),
                    ],
                )

            # Sección Destacados
            destacados = Column(
                spacing=10,
                controls=[
                    Text("Destacados", size=20, weight=FontWeight.BOLD, color="white"),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            producto("assets/prod1.jpg", "Hatsune Miku", 199),
                            producto("assets/prod2.jpg", "Lesbianas", 249),
                            producto("assets/prod3.jpg", "El wey de la motosierra", 299),
                        ],
                    )
                ],
            )

            destacados_container = Container(
                content=destacados,
                padding=ft.padding.symmetric(vertical=20),
                alignment=alignment.center,
            )

            # Sección Novedades (misma estructura)
            novedades = Column(
                spacing=10,
                controls=[
                    Text("Novedades", size=20, weight=FontWeight.BOLD, color="white"),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            producto("assets/prod1.jpg", "Hatsune Miku", 199),
                            producto("assets/prod2.jpg", "Lesbianas", 249),
                            producto("assets/prod3.jpg", "El wey de la motosierra", 299),
                        ],
                    )
                ],
            )

            novedades_container = Container(
                content=novedades,
                padding=ft.padding.symmetric(vertical=20),
                alignment=alignment.center,
            )

            # Agregamos todo a la página
            self.page.add(
            Container(
            content=Column(
                spacing=0,
                controls=[
                    imagen,
                    categorias,
                    categorias_container,
                    destacados_container,
                    novedades_container
                ],
            ),
            bgcolor="#383838",  # <-- Esto asegura que todo el fondo sea gris oscuro
            expand=True,        
        )
    )


            self.page.update()

        except Exception:
            print("Excepción al construir la UI:", file=sys.stderr)
            traceback.print_exc()
            self.page.controls.clear()
            self.page.add(Text("Ocurrió un error al cargar la interfaz. Revisa la consola.", color="red"))
            self.page.update()
