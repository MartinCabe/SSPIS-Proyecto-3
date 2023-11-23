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
from backend.usuarios import Usuario

class MainWindow:
    def __init__(self, root):
        self.usuario_logeado = Usuario((0, 0, '', '', '', '', '', '', '')) # Probablemente sea una pendejada, solo esperemos que no rompa nada
        self.root = root
        self.root.title("Control Escolar")
        self.root.geometry("1000x700")
        self.pestanas = ttk.Notebook(self.root)
        frame_login = Login(self.pestanas,self)
        frame_usuarios = Usuarios(self.pestanas)
        self.frame_alumnos = Alumnos(self.pestanas, self.usuario_logeado)
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
        self.pestanas.add(self.frame_alumnos, text = "Alumnos")
        self.pestanas.add(frame_maestros, text = "Maestros")
        self.pestanas.add(frame_materias, text = "Materias")
        self.pestanas.add(frame_grupos, text = "Grupos")
        self.pestanas.add(frame_salon, text = "Salon")
        self.pestanas.add(frame_horario, text = "Horarios")
        self.pestanas.add(frame_carrera, text = "Carrera")
        self.pestanas.add(frame_planeacion, text = "Planeacion")
        self.pestanas.add(frame_logout, text = "Logout")
        
        self.pestanas.pack(fill="both", expand=True)
         # Enlaza el evento de cambio de pestaña
        self.pestanas.bind("<<NotebookTabChanged>>", lambda event: self.actualizar_pestanas())
        
    def actualizar_pestanas(self):
        self.usuario_logeado = self.pestanas.winfo_children()[0].get_usuario_logeado()
        if self.usuario_logeado:
            self.pestanas.tab(0, state="hidden")
            for i in range(1, self.pestanas.index("end")):
                if self.usuario_logeado.perfil==1:
                    self.pestanas.tab(i, state="normal")
                elif self.usuario_logeado.perfil == 2:
                    self.pestanas.tab(2, state="normal")
                    self.pestanas.tab(3, state="normal")
                    self.pestanas.tab(10, state="normal")
                elif self.usuario_logeado.perfil == 3:
                    self.frame_alumnos.actualizar_sesion(self.usuario_logeado)
                    self.pestanas.tab(2, state = "normal")
                    self.pestanas.tab(10, state = "normal")
        else:
            for i in range(1,self.pestanas.index("end")):
                self.pestanas.tab(i, state="hidden")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
