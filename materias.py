import tkinter as tk
import re
from backend.materias import get_max_id, get_nombres_carreras, post_materia, Materia, get_materia, update_materia, delete_materia
from tkinter import ttk, END, messagebox

def validar_cadena(cadena):
    if re.match('^[a-zA-Z\s]+$', cadena):
        return cadena
    else:
        raise ValueError("Cadena tiene caracteres invalidos")

class Materias(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.carreras = get_nombres_carreras()
        self.carrera_a_id = {record[1]: record[0] for record in self.carreras}
        # ----- WIDGETS -----

        # Labels
        tk.Label(self, text = "Ingrese codigo materia").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Asignatura").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Creditos").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Semestre").grid(row = 4, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Carrera").grid(row = 2, column = 2, padx = 10, pady = 10)

        # Entries
        self.entry_materias_buscar = tk.Entry(self)
        self.entry_materias_id = tk.Entry(self)
        self.entry_materias_asignatura = tk.Entry(self)
        self.entry_materias_creditos = tk.Entry(self)
        self.entry_materias_semestre = tk.Entry(self)

        self.entry_materias_buscar.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_materias_id.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.entry_materias_asignatura.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.entry_materias_creditos.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.entry_materias_semestre.grid(row = 4, column = 1, padx = 10, pady = 10)

        # Combo Box
        self.combo_materias_carrera = ttk.Combobox(self)

        self.combo_materias_carrera.grid(row = 2, column = 3, padx = 10, pady = 10)

        self.combo_materias_carrera['values'] = [record[1] for record in self.carreras]

        self.combo_materias_carrera.bind("<<ComboboxSelected>>", self.carrera_select)

        # Buttons
        self.button_materias_buscar = tk.Button(self, text = "Buscar", command = lambda: self.buscar_materia())
        self.button_materias_nuevo = tk.Button(self, text = "Nuevo", command = lambda: self.nueva_materia())
        self.button_materias_guardar = tk.Button(self, text = "Guardar", command = lambda: self.guardar_materia())
        self.button_materias_cancelar = tk.Button(self, text = "Cancelar", command = lambda: self.limpiar_campos())
        self.button_materias_editar = tk.Button(self, text = "Editar")
        self.button_materias_baja = tk.Button(self, text = "Baja")

        self.button_materias_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_materias_nuevo.grid(row = 5, column = 0, padx = 10, pady = 10)
        self.button_materias_guardar.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.button_materias_cancelar.grid(row = 5, column = 2, padx = 10, pady = 10)
        self.button_materias_editar.grid(row = 5, column = 3, padx = 10, pady = 10)
        self.button_materias_baja.grid(row = 5, column = 4, padx = 10, pady = 10)

        self.entry_materias_id.config(state = "disabled")

    def nueva_materia(self):
        self.limpiar_campos()
        self.entry_materias_id.config(state = "normal")
        self.entry_materias_id.insert(0, int(get_max_id()[0]) + 1)
        self.entry_materias_id.config(state = "disabled")

    def limpiar_campos(self):
        self.entry_materias_buscar.delete(0, END)
        self.entry_materias_id.config(state = "normal")
        self.entry_materias_id.delete(0, END)
        self.entry_materias_id.config(state = "disabled")
        self.entry_materias_asignatura.delete(0, END)
        self.entry_materias_creditos.delete(0, END)
        self.entry_materias_semestre.delete(0, END)
        self.combo_materias_carrera.set('')

    def carrera_select(self, event):
        carrera = self.combo_materias_carrera.get()
        global carrera_id
        if carrera is not None:
            carrera_id = self.carrera_a_id.get(carrera)
            print(carrera_id)

    def guardar_materia(self):
        try:
            post_materia(
                validar_cadena(self.entry_materias_asignatura.get()),
                int(self.entry_materias_semestre.get()),
                int(self.entry_materias_creditos.get()),
                carrera_id
            )
            messagebox.showinfo(title = "Aviso", message = f"Materia guardada con el id: {int(get_max_id()[0])}")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")

    def buscar_materia(self):
        try:
            materia = Materia(get_materia(int(self.entry_materias_buscar.get())))
            self.limpiar_campos()
            self.entry_materias_id.config(state = "normal")
            self.colocar_datos_en_entrys(materia)
            self.entry_materias_id.config(state = "disabled")
            self.button_materias_editar.config(command=lambda:self.editar_materia(materia.id))
            self.button_materias_baja.config(command=lambda:self.borrar_materia(materia.id))
        except:
            messagebox.showerror(title = "Error", message = "Dato de busqueda invalido")

    def colocar_datos_en_entrys(self, materia):
        self.entry_materias_id.insert(0, materia.id)
        self.entry_materias_asignatura.insert(0, materia.asignatura)
        self.entry_materias_creditos.insert(0, materia.creditos)
        self.entry_materias_semestre.insert(0, materia.semestre)
        self.combo_materias_carrera.set(materia.carrera)
    
    def editar_materia(self, id):
        try:
            global carrera_id
            materia = Materia((id, validar_cadena(self.entry_materias_asignatura.get()),
            int(self.entry_materias_semestre.get()),
            int(self.entry_materias_creditos.get()),
            carrera_id,
            'ACTIVO'))
            update_materia(id,materia)
            messagebox.showinfo(title = "Aviso", message = "Materia editada con exito")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")

    def borrar_materia(self, id):
        confirmar = messagebox.askyesno(title = "Confirmacion", message = f"¿Estás seguro de eliminar la materia con el id: {id} ?")
        if confirmar:
            delete_materia(id)
            messagebox.showinfo(title = "Aviso", message = "Materia eliminada con exito")
            self.limpiar_campos()
        else:
            messagebox.showerror(title = "Error", message = "Operacion cancelada")