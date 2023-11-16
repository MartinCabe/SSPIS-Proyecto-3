import tkinter as tk
from tkinter import ttk

class Salon(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Ingrese codigo Salon").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Edificio").grid(row = 3, column = 0, padx = 10, pady = 10)

        self.label_salon_id = tk.Label(self)
        self.label_salon_id.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Entries
        self.entry_salon_buscar = tk.Entry(self)
        self.entry_salon_nombre = tk.Entry(self)
        self.entry_salon_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_salon_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Combo boxes
        self.combo_salon_edificio = ttk.Combobox(self, values=['A', 'B', 'C', 'D', 'F', 'G'])
        self.combo_salon_edificio.grid(row = 3, column = 1, padx = 10, pady = 10)

        # Buttons
        self.button_salon_buscar = tk.Button(self, text = "Buscar")
        self.button_salon_nuevo = tk.Button(self, text = "Nuevo")
        self.button_salon_guardar = tk.Button(self, text = "Guardar")
        self.button_salon_cancelar = tk.Button(self, text = "Cancelar")
        self.button_salon_editar = tk.Button(self, text = "Editar")
        self.button_salon_baja = tk.Button(self, text = "Baja")
        self.button_salon_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_salon_nuevo.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.button_salon_guardar.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.button_salon_cancelar.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.button_salon_editar.grid(row = 4, column = 3, padx = 10, pady = 10)
        self.button_salon_baja.grid(row = 4, column = 4, padx = 10, pady = 10)
