import tkinter as tk
from tkinter import ttk

class Alumnos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Ingrese codigo de alumno:").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID:").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre:").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Paterno:").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Materno:").grid(row = 4, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "E-Mail:").grid(row = 5, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Estado:").grid(row = 1, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Fecha Nac:").grid(row = 2, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Carrera:").grid(row = 3, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Materias:").grid(row = 4, column = 2, padx = 10, pady = 10)

        # Entries
        self.entry_alumnos_buscar = tk.Entry(self)
        self.entry_alumnos_id = tk.Entry(self)
        self.entry_alumnos_nombre = tk.Entry(self)
        self.entry_alumnos_paterno = tk.Entry(self)
        self.entry_alumnos_materno = tk.Entry(self)
        self.entry_alumnos_email = tk.Entry(self)
        self.entry_alumnos_nacimiento = tk.Entry(self)
        self.entry_alumnos_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_id.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_paterno.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_materno.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_email.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_nacimiento.grid(row = 2, column = 3, padx = 10, pady = 10)

        # Combo Boxes
        self.combo_alumnos_estado = ttk.Combobox(self) # Estados de Mexico
        self.combo_alumnos_carrera = ttk.Combobox(self)
        self.combo_alumnos_materia = ttk.Combobox(self)
        self.combo_alumnos_estado.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.combo_alumnos_carrera.grid(row = 3, column = 3, padx = 10, pady = 10)
        self.combo_alumnos_materia.grid(row = 4, column = 3, padx = 10, pady = 10)

        # List Box
        self.list_alumnos_materias = tk.Listbox(self)
        self.list_alumnos_materias.grid(row = 5, column = 3, padx = 10, pady = 10)

        # Buttons
        self.button_alumnos_buscar = tk.Button(self, text = "Buscar")
        self.button_alumnos_nuevo = tk.Button(self, text = "Nuevo")
        self.button_alumnos_guardar = tk.Button(self, text = "Guardar")
        self.button_alumnos_cancelar = tk.Button(self, text = "Cancelar")
        self.button_alumnos_editar = tk.Button(self, text = "Editar")
        self.button_alumnos_baja = tk.Button(self, text = "Baja")
        self.button_alumnos_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_alumnos_nuevo.grid(row = 6, column = 0, padx = 10, pady = 10)
        self.button_alumnos_guardar.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.button_alumnos_cancelar.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_alumnos_editar.grid(row = 6, column = 3, padx = 10, pady = 10)
        self.button_alumnos_baja.grid(row = 6, column = 4, padx = 10, pady = 10)

        self.entry_alumnos_id.config(state = "disabled")
        self.entry_alumnos_nombre.config(state = "disabled")
        self.entry_alumnos_paterno.config(state = "disabled")
        self.entry_alumnos_materno.config(state = "disabled")
        self.entry_alumnos_email.config(state = "disabled")