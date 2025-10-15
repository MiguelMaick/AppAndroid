import flet as ft
from flet import (
    Page, TextField, ElevatedButton, Text, Column, 
    Container, alignment
)
from clientes_model import ClientesModel
from components import create_appbar

class VistaRegistro:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Soy Nuevo"
        self.page.clean()
        self.page.appbar = create_appbar(self.page)

        self.modelo = ClientesModel()

        # Definición de todos los campos del formulario
        self.lbl_message2 = Text("Ingresa tus datos")
        self.txt_Nombre = TextField(label="Nombre", width=300)
        self.txt_appat = TextField(label="Apellido Paterno", width=300)
        self.txt_apmat = TextField(label="Apellido Materno", width=300)
        self.txt_email = TextField(label="Email", width=300)
        self.txt_password2 = TextField(label="Contraseña", password=True, width=300)
        self.txt_telefono = TextField(label="Teléfono", width=300)
        self.txt_domicilio = TextField(label="Domicilio", width=300)
        self.txt_codigo_postal = TextField(label="Código Postal", width=300)
        self.txt_municipio = TextField(label="Municipio", width=300)
        self.btn_registro = ElevatedButton(
            text="Registrar", 
            on_click=self.registro, 
            bgcolor="#f8b204", 
            color="black"
        )

        # Se agrupan todos los controles en una Columna
        formulario_registro = Column(
            controls=[
                self.lbl_message2,
                self.txt_Nombre,
                self.txt_appat,
                self.txt_apmat,
                self.txt_email,
                self.txt_password2,
                self.txt_telefono,
                self.txt_domicilio,
                self.txt_codigo_postal,
                self.txt_municipio,
                self.btn_registro
            ],
            spacing=12,
            horizontal_alignment="center",
            scroll="auto",  # <-- AQUÍ SE AÑADE EL SCROLL pero por alguna razón no funciona bien, solo en pantalla completa XD
            expand=True
        )
        
        # Se envuelve todo en un Container para centrarlo en la página
        contenedor_centrado = Container(
        content=formulario_registro,
        alignment=alignment.center,
        )

        self.page.add(contenedor_centrado)

    def registro(self, e):
        # el resto de la función de registro no cambia
        cliente = {
            "nombre": self.txt_Nombre.value,
            "paterno": self.txt_appat.value,
            "materno": self.txt_apmat.value,
            "email": self.txt_email.value,
            "password": self.txt_password2.value,
            "telefono": self.txt_telefono.value,
            "domicilio": self.txt_domicilio.value,
            "codigo_postal": self.txt_codigo_postal.value,
            "municipio": self.txt_municipio.value
        }

        id_insertado = self.modelo.agregar_cliente(cliente)
        self.lbl_message2.value = f"Usuario registrado con ID: {id_insertado}"
        self.lbl_message2.color = "green"
        self.page.update()
        self.page.go("/catalogo")