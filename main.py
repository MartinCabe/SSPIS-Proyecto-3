import tkinter as tk
from tkinter import ttk
from login import Login
from usuarios import Usuarios
from alumnos import Alumnos
from maestros import Maestros
from materias import Materias
from grupos import Grupos
from horario import Horario
from salon import Salon
from carrera import Carrera
from planeacion import Planeacion
from logout import Logout

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Escolar")
        self.root.geometry("1000x700")
        self.pestanas = ttk.Notebook(self.root)

        frame_login = Login(self.pestanas)
        frame_usuarios = Usuarios(self.pestanas)
        frame_alumnos = Alumnos(self.pestanas)
        frame_maestros = Maestros(self.pestanas)
        frame_materias = Materias(self.pestanas)
        frame_grupos = Grupos(self.pestanas)
        frame_horario = Horario(self.pestanas)
        frame_salon = Salon(self.pestanas)
        frame_carrera = Carrera(self.pestanas)
        frame_planeacion = Planeacion(self.pestanas)
        frame_logout = Logout(self.pestanas)

        self.pestanas.add(frame_login, text = "Login")
        self.pestanas.add(frame_usuarios, text = "Usuarios")
        self.pestanas.add(frame_alumnos, text = "Alumnos")
        self.pestanas.add(frame_maestros, text = "Maestros")
        self.pestanas.add(frame_materias, text = "Materias")
        self.pestanas.add(frame_grupos, text = "Horarios")
        self.pestanas.add(frame_salon, text = "Salon")
        self.pestanas.add(frame_carrera, text = "Carrera")
        self.pestanas.add(frame_planeacion, text = "Planeacion")
        self.pestanas.add(frame_logout, text = "Logout")
        
        self.pestanas.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
