import flet as ft

def create_appbar(page: ft.Page):
    return ft.AppBar(
        bgcolor="#f8b204",
        center_title=False,
        title=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # LADO IZQUIERDO  Menú Popup
                ft.PopupMenuButton(
                    icon_color="black",
                    items=[
                        ft.PopupMenuItem(text="Login", on_click=lambda e: page.go("/login")),
                        ft.PopupMenuItem(text="Soy nuevo", on_click=lambda e: page.go("/registro")),
                        ft.PopupMenuItem(text="Home", on_click=lambda e: page.go("/home")),
                        ft.PopupMenuItem(text="Catálogo", on_click=lambda e: page.go("/catalogo")),
                    ],
                ),

                # CENTRO Logo
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src="assets/logoB.png",
                        width=100,
                        height=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                ),

                # LADO DERECHO Iconos (Buscar + Carrito)
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.SEARCH,
                            icon_color="black",
                            tooltip="Buscar",
                            on_click=lambda e: print("Buscar presionado"),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.SHOPPING_CART,
                            icon_color="black",
                            tooltip="Carrito",
                            on_click=lambda e: page.go("/carrito"),
                        ),
                    ],
                ),
            ],
        ),
    )
