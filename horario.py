import tkinter as tk
from tkinter import ttk

class Horario(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----   
        # Entries
        tk.Label(self, text = "Ingrese codigo Horario").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Turno").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Hora inicio").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Hora final").grid(row = 4, column = 0, padx = 10, pady = 10)

        self.label_horario_id = tk.Label(self)
        self.label_horario_id.grid(row = 1, column = 1)

        # Entries
        self.entry_horario_buscar = tk.Entry(self)
        self.entry_horario_inicio = tk.Entry(self)
        self.entry_horario_final = tk.Entry(self)
        self.entry_horario_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_horario_inicio.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.entry_horario_final.grid(row = 4, column = 1, padx = 10, pady = 10)

        # Combo boxes
        self.combo_horario_turno = ttk.Combobox(self, values=['M', 'V'])
        self.combo_horario_turno.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Buttons
        self.button_horario_buscar = tk.Button(self, text = "Buscar")
        self.button_horario_nuevo = tk.Button(self, text = "Nuevo")
        self.button_horario_guardar = tk.Button(self, text = "Guardar")
        self.button_horario_cancelar = tk.Button(self, text = "Cancelar")
        self.button_horario_editar = tk.Button(self, text = "Editar")
        self.button_horario_baja = tk.Button(self, text = "Baja")
        self.button_horario_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_horario_nuevo.grid(row = 5, column = 0, padx = 10, pady = 10)
        self.button_horario_guardar.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.button_horario_cancelar.grid(row = 5, column = 2, padx = 10, pady = 10)
        self.button_horario_editar.grid(row = 5, column = 3, padx = 10, pady = 10)
        self.button_horario_baja.grid(row = 5, column = 4, padx = 10, pady = 10)