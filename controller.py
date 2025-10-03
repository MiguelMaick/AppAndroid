from model import add_user, authenticate_user

class LoginController:
    def __init__(self,view):
        self.view = view
        
        def login()