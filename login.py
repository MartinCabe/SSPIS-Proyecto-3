import tkinter as tk

class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        tk.Label(self, text = "Contenido").grid(row = 0, column = 0)