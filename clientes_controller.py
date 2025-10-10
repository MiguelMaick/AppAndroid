from clientes_model import ClientesModel

class ClientesController:
    def __init__(self, view):
        self.view = view
        self.modelo = ClientesModel()

    def login(self):
        email = self.view.txt_email.value
        password = self.view.txt_password.value

        if self.modelo.autenticar_cliente(email, password):
            self.view.lbl_message.value = f"Bienvenido, {email}"
            self.view.lbl_message.color = "green"
        else:
            self.view.lbl_message.value = "Credenciales inválidas"
            self.view.lbl_message.color = "red"

        self.view.page.update()