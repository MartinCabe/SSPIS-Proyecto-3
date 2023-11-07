import tkinter as tk
import re
from tkinter import END, messagebox
from backend.carrera import get_max_id, post_carrera, Carreras, get_carrera, update_carrera, delete_carrera

def validar_cadena(cadena):
    if re.match('^[a-zA-Z\s]+$', cadena):
        return cadena
    else:
        raise ValueError("Cadena tiene caracteres invalidos")

class Carrera(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Ingrese codigo carrera").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Numero de semestres").grid(row = 3, column = 0, padx = 10, pady = 10)

        # Entries
        self.entry_carrera_buscar = tk.Entry(self)
        self.entry_carrera_id = tk.Entry(self)
        self.entry_carrera_nombre = tk.Entry(self)
        self.entry_carrera_semestres = tk.Entry(self)
        self.entry_carrera_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_carrera_id.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.entry_carrera_nombre.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.entry_carrera_semestres.grid(row = 3, column = 1, padx = 10, pady = 10)

        # Buttons
        self.button_carrera_buscar = tk.Button(self, text = "Buscar", command = lambda: self.buscar_carrera())
        self.button_carrera_nuevo = tk.Button(self, text = "Nuevo", command = lambda: self.nueva_carrera())
        self.button_carrera_guardar = tk.Button(self, text = "Guardar", command = lambda: self.guardar_carrera())
        self.button_carrera_cancelar = tk.Button(self, text = "Cancelar", command = lambda: self.limpiar_campos())
        self.button_carrera_editar = tk.Button(self, text = "Editar")
        self.button_carrera_baja = tk.Button(self, text = "Baja")
        self.button_carrera_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_carrera_nuevo.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.button_carrera_guardar.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.button_carrera_cancelar.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.button_carrera_editar.grid(row = 4, column = 3, padx = 10, pady = 10)
        self.button_carrera_baja.grid(row = 4, column = 4, padx = 10, pady = 10)

        self.entry_carrera_id.config(state = "disabled")

    def nueva_carrera(self):
        self.limpiar_campos()
        self.entry_carrera_id.config(state = "normal")
        self.entry_carrera_id.insert(0, int(get_max_id()[0]) + 1)
        self.entry_carrera_id.config(state = "disabled")

    def limpiar_campos(self):
        self.entry_carrera_buscar.delete(0, END)
        self.entry_carrera_id.config(state = "normal")
        self.entry_carrera_id.delete(0, END)
        self.entry_carrera_id.config(state = "disabled")
        self.entry_carrera_nombre.delete(0, END)
        self.entry_carrera_semestres.delete(0, END)

    def guardar_carrera(self):
        try:
            post_carrera(
                validar_cadena(self.entry_carrera_nombre.get()),
                int(self.entry_carrera_semestres.get())
            )
            messagebox.showinfo(title = "Aviso", message = f"Carrera guardada con el id: {int(get_max_id()[0])}")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")
    
    def buscar_carrera(self):
        try:
            carrera = Carreras(get_carrera(int(self.entry_carrera_buscar.get())))
            self.limpiar_campos()
            self.entry_carrera_id.config(state = "normal")
            self.colocar_datos_en_entrys(carrera)
            self.entry_carrera_id.config(state = "disabled")
            self.button_carrera_editar.config(command = lambda: self.editar_carrera(carrera.id))
            self.button_carrera_baja.config(command = lambda: self.borrar_carrera(carrera.id))
        except:
            messagebox.showerror(title = "Error", message = "Datos de busqueda invalido")
    
    def colocar_datos_en_entrys(self, carrera):
        self.entry_carrera_id.insert(0, carrera.id)
        self.entry_carrera_nombre.insert(0, carrera.nombre)
        self.entry_carrera_semestres.insert(0, carrera.semestres)

    def editar_carrera(self, id):
        try:
            carrera = Carreras((id,
            validar_cadena(self.entry_carrera_nombre.get()),
            int(self.entry_carrera_semestres.get()),
            'ACTIVO'))
            update_carrera(id, carrera)
            messagebox.showinfo(title = "Aviso", message = "Carrera editada con exito")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")
    
    def borrar_carrera(self, id):
        confirmar = messagebox.askyesno(title = "Confirmacion", message = f"¿Estás seguro de eliminar la carrera con el id: {id} ?")
        if confirmar:
            delete_carrera(id)
            messagebox.showinfo(title = "Aviso", message = "Carrera eliminada con exito")
            self.limpiar_campos()
        else:
            messagebox.showerror(title = "Error", message = "Operacion cancelada")