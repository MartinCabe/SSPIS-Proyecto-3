import tkinter as tk

class Planeacion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.button_planeacion_generar = tk.Button(self, text = "Generar Planeacion")
        self.button_planeacion_generar.grid(row = 0, column = 0)