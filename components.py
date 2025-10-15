import flet as ft

def create_appbar(page: ft.Page):
    return ft.AppBar(
        leading=ft.IconButton(ft.Icons.HOME, icon_color="black", on_click=lambda e: page.go("/home")),
        leading_width=50,
        center_title=True,   # Esto centra el contenido del título
        title=ft.Container(
            content=ft.Image(
                src="assets/logo.png",
                width=100,
                height=50,
                fit=ft.ImageFit.CONTAIN,
            ),
            alignment=ft.alignment.center
        ),
        bgcolor="#f8b204",
        actions=[
            ft.PopupMenuButton(
                icon_color="black",
                items=[
                    ft.PopupMenuItem(text="Login", on_click=lambda e: page.go("/login")),
                    ft.PopupMenuItem(text="Soy nuevo", on_click=lambda e: page.go("/registro")),
                    ft.PopupMenuItem(text="Home", on_click=lambda e: page.go("/home")),
                ]
            ),
        ],
    )
