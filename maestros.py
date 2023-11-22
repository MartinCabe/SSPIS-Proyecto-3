import tkinter as tk
import re
from backend.maestro import get_max_id, get_nombres_carreras,get_nombres_materias, post_maestro, Maestro, get_maestro, update_maestro, delete_maestro
from tkinter import ttk, END, messagebox

def validar_cadena(cadena):
    if re.match('^[a-zA-Z\s]+$', cadena):
        return cadena
    else:
        raise ValueError("Cadena tiene caracteres inválidos")

class Maestros(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.carreras = get_nombres_carreras()
        self.materias = get_nombres_materias()
        self.carrera_a_id = {record[1]: record[0] for record in self.carreras}
        self.materia_a_id = {record[1]: record[0] for record in self.materias}
        # ----- WIDGETS -----

        # Labels
        tk.Label(self, text="Ingrese codigo del maestro").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="ID").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self, text="Nombre").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self, text="Apellido Paterno").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self, text="Apellido Materno").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self, text="Correo").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(self, text="Carrera").grid(row=6, column=0, padx=10, pady=10)
        tk.Label(self, text="Materia").grid(row=7, column=0, padx=10, pady=10)
        tk.Label(self, text="Grado de Estudio").grid(row=8, column=0, padx=10, pady=10)

        # Entries
        self.entry_maestro_buscar = tk.Entry(self)
        self.entry_maestros_id = tk.Entry(self)
        self.entry_maestros_nombre = tk.Entry(self)
        self.entry_maestros_apellido_paterno = tk.Entry(self)
        self.entry_maestros_apellido_materno = tk.Entry(self)
        self.entry_maestros_correo = tk.Entry(self)
        self.entry_maestros_materia = tk.Entry(self)
        self.entry_maestros_grado_estudio = tk.Entry(self)
        self.entry_maestros_carrera = tk.Entry(self)
        self.entry_maestros_id.config(state="disabled")

        self.entry_maestro_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_maestros_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_maestros_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.entry_maestros_apellido_paterno.grid(row=3, column=1, padx=10, pady=10)
        self.entry_maestros_apellido_materno.grid(row=4, column=1, padx=10, pady=10)
        self.entry_maestros_correo.grid(row=5, column=1, padx=10, pady=10)
        self.entry_maestros_carrera.grid(row=6, column=1, padx=10, pady=10)
        self.entry_maestros_materia.grid(row=7, column=1, padx=10, pady=10)
        self.entry_maestros_grado_estudio.grid(row=8, column=1, padx=10, pady=10)

        # Combo Box
        self.combo_maestros_carrera = ttk.Combobox(self)

        self.combo_maestros_carrera.grid(row=6, column=1, padx=10, pady=10)

        self.combo_maestros_carrera['values'] = [record[1] for record in self.carreras]

        self.combo_maestros_carrera.bind("<<ComboboxSelected>>", self.carrera_select)

        self.combo_maestros_materia = ttk.Combobox(self)

        self.combo_maestros_materia.grid(row=7, column=1, padx=10, pady=10)

        self.combo_maestros_materia['values'] = [record[1] for record in self.materias]

        self.combo_maestros_materia.bind("<<ComboboxSelected>>", self.materia_select)

        # Buttons
        self.button_buscar_maestro = tk.Button(self, text = "Buscar", command = lambda: self.buscar_maestro())
        self.button_maestros_nuevo = tk.Button(self, text="Nuevo", command=lambda: self.nuevo_maestro())
        self.button_maestros_guardar = tk.Button(self, text="Guardar", command=lambda: self.guardar_maestro())
        self.button_maestros_cancelar = tk.Button(self, text="Cancelar", command=lambda: self.limpiar_campos())
        self.button_maestros_editar = tk.Button(self, text="Editar")
        self.button_maestros_baja = tk.Button(self, text="Baja")

        self.button_buscar_maestro.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_maestros_nuevo.grid(row=9, column=0, padx=10, pady=10)
        self.button_maestros_guardar.grid(row=9, column=1, padx=10, pady=10)
        self.button_maestros_cancelar.grid(row=9, column=2, padx=10, pady=10)
        self.button_maestros_editar.grid(row=9, column=3, padx=10, pady=10)
        self.button_maestros_baja.grid(row=9, column=4, padx=10, pady=10)

        

    def nuevo_maestro(self):
        self.limpiar_campos()
        self.entry_maestros_id.config(state="normal")
        self.entry_maestros_id.insert(0, int(get_max_id()[0]) + 1)
        self.entry_maestros_id.config(state="disabled")

    def limpiar_campos(self):
        self.entry_maestros_id.config(state="normal")
        self.entry_maestros_id.delete(0, END)
        self.entry_maestros_id.config(state="disabled")
        self.entry_maestros_nombre.delete(0, END)
        self.entry_maestros_apellido_paterno.delete(0, END)
        self.entry_maestros_apellido_materno.delete(0, END)
        self.entry_maestros_correo.delete(0, END)
        self.entry_maestros_grado_estudio.delete(0, END)
        self.combo_maestros_carrera.set('')
        self.combo_maestros_materia.set('')

    def carrera_select(self, event):
        carrera = self.combo_maestros_carrera.get()
        global carrera_id
        if carrera is not None:
            carrera_id = self.carrera_a_id.get(carrera)

    def materia_select(self, event):
        materia = self.combo_maestros_materia.get()
        global materia_id
        if materia is not None:
            materia_id = self.materia_a_id.get(materia)

    def guardar_maestro(self):
        try:
            post_maestro(
                validar_cadena(self.entry_maestros_nombre.get()),
                validar_cadena(self.entry_maestros_apellido_paterno.get()),
                validar_cadena(self.entry_maestros_apellido_materno.get()),
                self.entry_maestros_correo.get(),
                carrera_id,
                materia_id,
                self.entry_maestros_grado_estudio.get()
            )
            messagebox.showinfo(title="Aviso", message=f"Maestro guardado con el id: {int(get_max_id()[0])}")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror(title="Error", message="Datos inválidos o incompletos")

    def buscar_maestro(self):
        try:
            maestro = Maestro(get_maestro(int(self.entry_maestro_buscar.get())))
            self.limpiar_campos()
            self.entry_maestros_id.config(state = "normal")
            self.colocar_datos_en_entrys(maestro)
            self.entry_maestros_carrera.config(state = "disabled")
            self.button_maestros_editar.config(command=lambda:self.editar_maestro(maestro.id))
            self.button_maestros_baja.config(command=lambda:self.borrar_maestro(maestro.id))
        except:
            messagebox.showerror(title = "Error", message = "Dato de busqueda invalido")

    def colocar_datos_en_entrys(self, maestro):
        self.entry_maestros_id.insert(0, maestro.id)
        self.entry_maestros_nombre.insert(0,maestro.nombre)
        self.entry_maestros_apellido_paterno.insert(0, maestro.apellido_paterno)
        self.entry_maestros_apellido_materno.insert(0, maestro.apellido_materno)
        self.entry_maestros_grado_estudio.insert(0, maestro.grado_de_estudio)
        self.entry_maestros_correo.insert(0, maestro.correo)
        self.combo_maestros_carrera.set(maestro.carrera)
        self.combo_maestros_materia.set(maestro.materia)
    
    def editar_maestro(self, id):
        try:
            global carrera_id
            maestro = Maestro((id, validar_cadena(self.entry_maestros_nombre.get()),
            self.entry_maestros_apellido_paterno.get(),
            self.entry_maestros_apellido_materno.get(),
            self.entry_maestros_correo.get(),
            carrera_id,
            materia_id,
            self.entry_maestros_grado_estudio.get(),
            'ACTIVO'))
            update_maestro(id,maestro)
            messagebox.showinfo(title = "Aviso", message = "Maestro editado con exito")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")

    def borrar_maestro(self, id):
        confirmar = messagebox.askyesno(title = "Confirmacion", message = f"¿Estás seguro de eliminar al maestro con el id: {id} ?")
        if confirmar:
            delete_maestro(id)
            messagebox.showinfo(title = "Aviso", message = "Maestro eliminado con exito")
            self.limpiar_campos()
        else:
            messagebox.showerror(title = "Error", message = "Operacion cancelada")