import tkinter as tk
from backend.login import *
class Login(tk.Frame):
    usuario_logeado = None
    def __init__(self, parent,main):
        super().__init__(parent)
        self.parent = parent
        self.main = main
        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Usuario:").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Password: ").grid(row = 1, column = 0, padx = 10, pady = 10)

        # Entries
        entry_login_username = tk.Entry(self)
        entry_login_password = tk.Entry(self, show = "*")
        entry_login_username.grid(row = 0, column = 1, padx = 10, pady = 10)
        entry_login_password.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Buttons
        button_login_login = tk.Button(self, text = "Login")
        button_login_login.grid(row = 2, column = 0, padx = 10, pady = 10)
        button_login_login.config(command=lambda:self.set_usuario_logeado(entry_login_username.get(),entry_login_password.get()))

    def set_usuario_logeado(self,nombre_usuario,contraseña):
        self.usuario_logeado = logear_usuario(nombre_usuario,contraseña)
        self.main.actualizar_pestanas()
        print(self.usuario_logeado)
    
    def get_usuario_logeado(self):
        return self.usuario_logeado