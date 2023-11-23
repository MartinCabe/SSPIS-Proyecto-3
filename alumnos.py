import tkinter as tk
from tkinter import ttk, END, messagebox
from datetime import datetime
import backend.alumno as alu

def validar_fecha(fecha):
    try:
        objeto_fecha = datetime.strptime(fecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        raise ValueError("La cadena tiene un formato de fecha invalido AAAA-MM-DD")

class Alumnos(tk.Frame):
    def __init__(self, parent, logeado):
        super().__init__(parent)
        self.parent = parent
        self.usuario_logeado = logeado

        self.estados_mexico = [
            "Aguascalientes",
            "Baja California",
            "Baja California Sur",
            "Campeche",
            "Chiapas",
            "Chihuahua",
            "Coahuila",
            "Colima",
            "Durango",
            "Guanajuato",
            "Guerrero",
            "Hidalgo",
            "Jalisco",
            "México",
            "Michoacán",
            "Morelos",
            "Nayarit",
            "Nuevo León",
            "Oaxaca",
            "Puebla",
            "Querétaro",
            "Quintana Roo",
            "San Luis Potosí",
            "Sinaloa",
            "Sonora",
            "Tabasco",
            "Tamaulipas",
            "Tlaxcala",
            "Veracruz",
            "Yucatán",
            "Zacatecas"
        ]

        self.tupla_carreras = alu.get_carreras()
        self.carreras = {record[0]: record[1] for record in self.tupla_carreras}
        self.tupla_registradas = ()
        self.tupla_disponibles = ()
        self.dict_registradas = {}
        self.dict_disponibles = {}

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
        tk.Label(self, text = "AAAA-MM-DD").grid(row = 2, column = 4, padx = 10, pady = 10)
        tk.Label(self, text = "Materias disponibles").grid(row = 6, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Materias registradas").grid(row = 6, column = 3, padx = 10, pady = 10)

        self.label_alumnos_id = tk.Label(self)
        self.label_alumnos_nombre = tk.Label(self)
        self.label_alumnos_paterno = tk.Label(self)
        self.label_alumnos_materno = tk.Label(self)
        self.label_alumnos_email = tk.Label(self)
        self.label_alumnos_id.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.label_alumnos_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.label_alumnos_paterno.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.label_alumnos_materno.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.label_alumnos_email.grid(row = 5, column = 1, padx = 10, pady = 10)

        # Entries
        self.entry_alumnos_buscar = tk.Entry(self)
        self.entry_alumnos_nacimiento = tk.Entry(self)
        self.entry_alumnos_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_alumnos_nacimiento.grid(row = 2, column = 3, padx = 10, pady = 10)

        # Combo Boxes
        self.combo_alumnos_estado = ttk.Combobox(self, values = self.estados_mexico) # Estados de Mexico
        self.combo_alumnos_carrera = ttk.Combobox(self, values = list(self.carreras.values()))
        self.combo_alumnos_estado.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.combo_alumnos_carrera.grid(row = 3, column = 3, padx = 10, pady = 10)

        # List Box
        self.list_alumnos_disponibles = tk.Listbox(self)
        self.list_alumnos_registradas = tk.Listbox(self)
        self.list_alumnos_disponibles.grid(row = 7, column = 0, padx = 10, pady = 10)
        self.list_alumnos_registradas.grid(row = 7, column = 3, padx = 10, pady = 10)

        # Buttons
        self.button_alumnos_buscar = tk.Button(self, text = "Buscar", command = lambda: self.buscar_alumno())
        self.button_alumnos_datos = tk.Button(self, text = "Guardar datos de alumno", command = lambda: self.guardar_datos_alumno())
        self.button_alumnos_cancelar = tk.Button(self, text = "Cancelar", command = lambda: self.limpiar_campos())
        self.button_alumnos_registrar = tk.Button(self, text = "->", command = lambda: self.mover_a_registrar())
        self.button_alumnos_quitar = tk.Button(self, text = "<-", command = lambda: self.mover_a_disponibles())
        self.button_alumnos_materias = tk.Button(self, text = "Registrar materias", command = lambda: self.registrar_materias())
        
        self.button_alumnos_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_alumnos_datos.grid(row = 4, column = 3, padx = 10, pady = 10)
        self.button_alumnos_registrar.grid(row = 7, column = 1)
        self.button_alumnos_quitar.grid(row = 7, column = 2)
        self.button_alumnos_materias.grid(row = 8, column = 3, padx = 10, pady = 10)

    # ----- FUNCIONES -----

    def actualizar_sesion(self, nuevo):
        self.usuario_logeado = nuevo

    def buscar_alumno(self):
        try:
            self.limpiar_campos()
            id = int(self.entry_alumnos_buscar.get())
            usuario = alu.buscar_usuario(id)
            alumno = alu.buscar_alumno(id)
            self.label_alumnos_id.config(text = f"{id}")
            self.label_alumnos_nombre.config(text = f"{usuario[0]}")
            self.label_alumnos_paterno.config(text = f"{usuario[1]}")
            self.label_alumnos_materno.config(text = f"{usuario[2]}")
            self.label_alumnos_email.config(text = f"{usuario[3]}")
            if self.usuario_logeado.id != id and self.usuario_logeado.perfil == 3:
                self.button_alumnos_datos.config(state = "disabled")
                self.button_alumnos_registrar.config(state = "disabled")
                self.button_alumnos_quitar.config(state = "disabled")
                self.button_alumnos_materias.config(state = "disabled")
            else:
                self.button_alumnos_datos.config(state = "normal")
                self.button_alumnos_registrar.config(state = "normal")
                self.button_alumnos_quitar.config(state = "normal")
                self.button_alumnos_materias.config(state = "normal")
            if len(alumno) != 0:
                self.tupla_registradas = alu.get_materias_registradas(id)
                if self.usuario_logeado.perfil == 0:
                    self.button_alumnos_datos.config(state = "normal")
                    self.button_alumnos_registrar.config(state = "normal")
                    self.button_alumnos_quitar.config(state = "normal")
                    self.button_alumnos_materias.config(state = "normal")
                elif (self.usuario_logeado.perfil == 3 and len(self.tupla_registradas) > 0) or self.usuario_logeado.id != id:
                    self.button_alumnos_datos.config(state = "disabled")
                    self.button_alumnos_registrar.config(state = "disabled")
                    self.button_alumnos_quitar.config(state = "disabled")
                    self.button_alumnos_materias.config(state = "disabled")
                else:
                    self.button_alumnos_datos.config(state = "disabled")
                    self.button_alumnos_registrar.config(state = "normal")
                    self.button_alumnos_quitar.config(state = "normal")
                    self.button_alumnos_materias.config(state = "normal")
                self.combo_alumnos_estado.insert(0, alumno[0])
                self.combo_alumnos_carrera.insert(0, self.carreras[alumno[2]])
                self.entry_alumnos_nacimiento.insert(0, alumno[1])
                self.tupla_disponibles = alu.get_materias_disponibles(id)
                self.dict_registradas = {record[0]: record[1] for record in self.tupla_registradas}
                self.dict_disponibles = {record[0]: record[1] for record in self.tupla_disponibles}
                for clave, valor in self.dict_disponibles.items():
                    texto = f"{valor}"
                    self.list_alumnos_disponibles.insert(END, texto)
                for clave, valor in self.dict_registradas.items():
                    texto = f"{valor}"
                    self.list_alumnos_registradas.insert(END, texto)
        except:
            messagebox.showerror(title = 'Error', message = "Usuario no encontrado o no es un estudiante")
        
    def limpiar_campos(self):
        self.label_alumnos_id.config(text = "")
        self.label_alumnos_nombre.config(text = "")
        self.label_alumnos_paterno.config(text = "")
        self.label_alumnos_materno.config(text = "")
        self.label_alumnos_email.config(text = "")
        self.entry_alumnos_nacimiento.delete(0, END)
        self.combo_alumnos_estado.set("")
        self.combo_alumnos_carrera.set("")
        self.list_alumnos_disponibles.delete(0, END)
        self.list_alumnos_registradas.delete(0, END)

    def mover_a_registrar(self):
        materia = self.list_alumnos_disponibles.curselection()
        if materia:
            valor = self.list_alumnos_disponibles.get(materia[0])
            self.list_alumnos_registradas.insert(tk.END, valor)
            self.list_alumnos_disponibles.delete(materia[0])

    def mover_a_disponibles(self):
        materia = self.list_alumnos_registradas.curselection()
        if materia:
            valor = self.list_alumnos_registradas.get(materia[0])
            self.list_alumnos_disponibles.insert(tk.END, valor)
            self.list_alumnos_registradas.delete(materia[0])

    def guardar_datos_alumno(self):
        try:
            id = int(self.label_alumnos_id.cget("text"))
            alumno = alu.buscar_alumno(id)
            fecha = validar_fecha(self.entry_alumnos_nacimiento.get())
            carrera_nombre = self.combo_alumnos_carrera.get()
            estado = self.combo_alumnos_estado.get()
            for clave, valor in self.carreras.items():
                if valor == carrera_nombre:
                    carrera = clave
            if len(alumno) != 0:
                if alumno[2] != carrera:
                    confirmar = messagebox.askyesno(title = "Confirmacion", message = f"Se detecto que se esta cambiando la carrera del alumno, esta accion dara de baja al alumno de todas las materias a las que esta inscrito. ¿Desea continuar?")
                    if confirmar:
                        alu.editar_alumno(id, estado, fecha, carrera)
                        alu.limpiar_materias(id)
                        messagebox.showinfo(title = "Aviso", message = "Datos de alumno editados con exito")
                else:
                    alu.editar_alumno(id, estado, fecha, carrera)
                    messagebox.showinfo(title = "Aviso", message = "Datos de alumno editados con exito")
            else:
                alu.registrar_alumno(id, estado, fecha, carrera)
                messagebox.showinfo(title = "Aviso", message = "Datos de alumno registrados con exito")
                if self.usuario_logeado.perfil == 3:
                    self.button_alumnos_datos.config(state = "disabled")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")

    def registrar_materias(self):
        if self.list_alumnos_disponibles.size() == 0:
            return
        id = int(self.label_alumnos_id.cget("text"))
        materias_a_registrar = [self.list_alumnos_registradas.get(index) for index in range(self.list_alumnos_registradas.size())]
        id_materias_registrar = []
        for clave, valor in self.dict_disponibles.items():
            if valor in materias_a_registrar:
                id_materias_registrar.append(clave)
        for clave, valor in self.dict_registradas.items():
            if valor in materias_a_registrar:
                id_materias_registrar.append(clave)
        alu.limpiar_materias(id)
        for i in id_materias_registrar:
            alu.registrar_materia(id, i)
        messagebox.showinfo(title = "Aviso", message = "Materias registradas con exito")
        if self.usuario_logeado.perfil == 3:
            self.button_alumnos_materias.config(state = "disabled")
            self.button_alumnos_registrar.config(state = "disabled")
            self.button_alumnos_quitar.config(state = "disabled")
        self.limpiar_campos()
