import tkinter as tk
from tkinter import ttk

class Grupos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labesls
        tk.Label(self, text = "Ingresar ID de Grupo").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Fecha").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Carrera").grid(row = 4, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Materia").grid(row = 5, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Maestro").grid(row = 1, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Salon").grid(row = 2, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Horario").grid(row = 3, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Semestre").grid(row = 4, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Numero alumnos").grid(row = 5, column = 2, padx = 10, pady = 10)

        self.label_grupo_id = tk.Label(self) # Este label va a servir como los entry_id de las otras pestanas
        self.label_grupo_id.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Entries
        self.entry_grupo_buscar = tk.Entry(self)
        self.entry_grupo_nombre = tk.Entry(self)
        self.entry_grupo_fecha = tk.Entry(self)
        self.entry_grupo_semestre = tk.Entry(self)
        self.entry_grupo_alumnos = tk.Entry(self)
        self.entry_grupo_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_grupo_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.entry_grupo_fecha.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.entry_grupo_semestre.grid(row = 4, column = 3, padx = 10, pady = 10)
        self.entry_grupo_alumnos.grid(row = 5, column = 3, padx = 10, pady = 10)

        # Combo boxes
        self.combo_grupo_carrera = ttk.Combobox(self)
        self.combo_grupo_materia = ttk.Combobox(self)
        self.combo_grupo_maestro = ttk.Combobox(self)
        self.combo_grupo_salon = ttk.Combobox(self)
        self.combo_grupo_horario = ttk.Combobox(self)
        self.combo_grupo_carrera.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.combo_grupo_materia.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.combo_grupo_maestro.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.combo_grupo_salon.grid(row = 2, column = 3, padx = 10, pady = 10)
        self.combo_grupo_horario.grid(row = 3, column = 3, padx = 10, pady = 10)

        # Buttons
        self.button_grupo_buscar = tk.Button(self, text = "Buscar")
        self.button_grupo_nuevo = tk.Button(self, text = "Nuevo")
        self.button_grupo_guardar = tk.Button(self, text = "Guardar")
        self.button_grupo_cancelar = tk.Button(self, text = "Cancelar")
        self.button_grupo_editar = tk.Button(self, text = "Editar")
        self.button_grupo_baja = tk.Button(self, text = "Baja")
        self.button_grupo_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_grupo_nuevo.grid(row = 6, column = 0, padx = 10, pady = 10)
        self.button_grupo_guardar.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.button_grupo_cancelar.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_grupo_editar.grid(row = 6, column = 3, padx = 10, pady = 10)
        self.button_grupo_baja.grid(row = 6, column = 4, padx = 10, pady = 10)
