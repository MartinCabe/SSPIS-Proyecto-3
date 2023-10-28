import tkinter as tk

class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

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
