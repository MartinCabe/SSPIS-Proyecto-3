import tkinter as tk
from tkinter import ttk

class Usuarios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Ingrese codigo de usuario:").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID:").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre:").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Paterno:").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Materno:").grid(row = 4, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "E-Mail:").grid(row = 5, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre Usuario:").grid(row = 1, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Password:").grid(row = 2, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Perfil:").grid(row = 3, column = 2, padx = 10, pady = 10)

        # Entries
        entry_usuarios_buscar = tk.Entry(self)
        entry_usuarios_id = tk.Entry(self)
        entry_usuarios_nombre = tk.Entry(self)
        entry_usuarios_paterno = tk.Entry(self)
        entry_usuarios_materno = tk.Entry(self)
        entry_usuarios_email = tk.Entry(self)
        entry_usuarios_username = tk.Entry(self)
        entry_usuarios_password = tk.Entry(self)
        entry_usuarios_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        entry_usuarios_id.grid(row = 1, column = 1, padx = 10, pady = 10)
        entry_usuarios_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)
        entry_usuarios_paterno.grid(row = 3, column = 1, padx = 10, pady = 10)
        entry_usuarios_materno.grid(row = 4, column = 1, padx = 10, pady = 10)
        entry_usuarios_email.grid(row = 5, column = 1, padx = 10, pady = 10)
        entry_usuarios_username.grid(row = 1, column = 3, padx = 10, pady = 10)
        entry_usuarios_password.grid(row = 2, column = 3, padx = 10, pady = 10)

        # ComboBox
        combo_usuarios_perfil = ttk.Combobox(self)
        combo_usuarios_perfil.grid(row = 3, column = 3, padx = 10, pady = 10)

        # Buttons
        button_usuarios_buscar = tk.Button(self, text = "Buscar")
        button_usuarios_nuevo = tk.Button(self, text = "Nuevo")
        button_usuarios_guardar = tk.Button(self, text = "Guardar")
        button_usuarios_cancelar = tk.Button(self, text = "Cancelar")
        button_usuarios_editar = tk.Button(self, text = "Editar")
        button_usuarios_baja = tk.Button(self, text = "Baja")
        button_usuarios_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        button_usuarios_nuevo.grid(row = 6, column = 0, padx = 10, pady = 10)
        button_usuarios_guardar.grid(row = 6, column = 1, padx = 10, pady = 10)
        button_usuarios_cancelar.grid(row = 6, column = 2, padx = 10, pady = 10)
        button_usuarios_editar.grid(row = 6, column = 3, padx = 10, pady = 10)
        button_usuarios_baja.grid(row = 6, column = 4, padx = 10, pady = 10)