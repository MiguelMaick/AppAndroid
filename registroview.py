import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, MainAxisAlignment
from clientes_model import ClientesModel  # Asegúrate de tener este archivo

class VistaRegistro:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Soy Nuevo"
        self.page.clean()

        self.modelo = ClientesModel()

        self.lbl_message2 = Text("Ingresa tus datos", color="blue")
        self.txt_Nombre = TextField(label="Nombre", width=200)
        self.txt_appat = TextField(label="Apellido Paterno", width=200)
        self.txt_apmat = TextField(label="Apellido Materno", width=200)
        self.txt_email = TextField(label="Email", width=200)
        self.txt_password2 = TextField(label="Contraseña", password=True, width=200)
        self.txt_telefono = TextField(label="Telefono", width=200)
        self.txt_domicilio = TextField(label="Domicilio", width=300)
        self.txt_codigo_postal = TextField(label="Codigo Postal", width=200)
        self.txt_municipio = TextField(label="Municipio", width=200)
        self.btn_registro = ElevatedButton(text="Registrar", on_click=self.registro)

        self.page.add(
            Column(
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
                alignment=MainAxisAlignment.CENTER,
                spacing=20
            )
        )

    def registro(self, e):
        cliente = {
            "nombre": self.txt_Nombre.value,
            "apellido_paterno": self.txt_appat.value,
            "apellido_materno": self.txt_apmat.value,
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