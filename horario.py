import tkinter as tk
from tkinter import ttk
from backend.horario import get_max_id, post_horario, Horario, get_horario, update_horario, delete_horario
from tkinter import ttk, messagebox
import datetime

class Horario(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----   
        # Entries
        tk.Label(self, text="Ingrese código Horario").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="ID").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self, text="Turno").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self, text="Hora inicio").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self, text="Hora final").grid(row=4, column=0, padx=10, pady=10)

        self.label_horario_id = tk.Label(self)
        self.label_horario_id.grid(row=1, column=1)

        # Entries
        self.entry_horario_buscar = tk.Entry(self)
        self.entry_horario_inicio = tk.Entry(self)
        self.entry_horario_final = tk.Entry(self)
        self.entry_horario_buscar.grid(row=0, column=1, padx=10, pady=10)
        self.entry_horario_inicio.grid(row=3, column=1, padx=10, pady=10)
        self.entry_horario_final.grid(row=4, column=1, padx=10, pady=10)

        # Combo boxes
        self.combo_horario_turno = ttk.Combobox(self, values=['M', 'V'])
        self.combo_horario_turno.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.button_horario_buscar = tk.Button(self, text="Buscar", command=self.buscar_horario)
        self.button_horario_nuevo = tk.Button(self, text="Nuevo", command=self.nuevo_horario)
        self.button_horario_guardar = tk.Button(self, text="Guardar", command=self.guardar_horario)
        self.button_horario_cancelar = tk.Button(self, text="Cancelar", command=self.limpiar_campos)
        self.button_horario_editar = tk.Button(self, text="Editar", command=self.editar_horario)
        self.button_horario_baja = tk.Button(self, text="Baja", command=self.borrar_horario)
        self.button_horario_buscar.grid(row=0, column=2, padx=10, pady=10)
        self.button_horario_nuevo.grid(row=5, column=0, padx=10, pady=10)
        self.button_horario_guardar.grid(row=5, column=1, padx=10, pady=10)
        self.button_horario_cancelar.grid(row=5, column=2, padx=10, pady=10)
        self.button_horario_editar.grid(row=5, column=3, padx=10, pady=10)
        self.button_horario_baja.grid(row=5, column=4, padx=10, pady=10)

    def nuevo_horario(self):
        self.limpiar_campos()
        self.label_horario_id.config(text=int(get_max_id()[0]) + 1)

    def limpiar_campos(self):
        self.entry_horario_buscar.delete(0, tk.END)
        self.entry_horario_inicio.delete(0, tk.END)
        self.entry_horario_final.delete(0, tk.END)
        self.combo_horario_turno.set('')
        self.label_horario_id.config(text='')

    def buscar_horario(self):
        try:
            horario_data = get_horario(int(self.entry_horario_buscar.get()))
            if horario_data:
                self.limpiar_campos()
                self.label_horario_id.config(text=horario_data[0])
                self.entry_horario_inicio.insert(0, horario_data[2])
                self.entry_horario_final.insert(0, horario_data[3])
                self.combo_horario_turno.set(horario_data[1])
            else:
                messagebox.showerror(title="Error", message="ID de horario no encontrado")
        except:
            messagebox.showerror(title="Error", message="Dato de búsqueda inválido")

    def validar_hora(self, hora):
        try:
            datetime.datetime.strptime(hora, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def guardar_horario(self):
        hora_inicio = self.entry_horario_inicio.get()
        hora_final = self.entry_horario_final.get()

        if self.validar_hora(hora_inicio) and self.validar_hora(hora_final):
            hora_inicio_dt = datetime.datetime.strptime(hora_inicio, '%H:%M:%S')
            hora_final_dt = datetime.datetime.strptime(hora_final, '%H:%M:%S')

            if hora_inicio_dt < hora_final_dt:
                post_horario(
                    self.combo_horario_turno.get(),
                    hora_inicio,
                    hora_final
                )
                messagebox.showinfo(title="Aviso", message=f"Horario guardado con el id: {int(get_max_id()[0])}")
                self.limpiar_campos()
            else:
                messagebox.showerror(title="Error", message="La hora inicial debe ser menor que la hora final")
        else:
            messagebox.showerror(title="Error", message="Formato de hora inválido")
    def editar_horario(self):
        try:
            horario = Horario((
                int(self.label_horario_id.cget("text")),
                self.combo_horario_turno.get(),
                self.entry_horario_inicio.get(),
                self.entry_horario_final.get()
            ))
            update_horario(horario.id, horario)
            messagebox.showinfo(title="Aviso", message="Horario editado con éxito")
            self.limpiar_campos()
        except:
            messagebox.showerror(title="Error", message="Datos inválidos o incompletos")

    def borrar_horario(self):
        confirmar = messagebox.askyesno(
            title="Confirmación",
            message=f"¿Estás seguro de eliminar el horario con el id: {self.label_horario_id.cget('text')} ?"
        )
        if confirmar:
            delete_horario(int(self.label_horario_id.cget('text')))
            messagebox.showinfo(title="Aviso", message="Horario eliminado con éxito")
            self.limpiar_campos()
        else:
            messagebox.showerror(title="Error", message="Operación cancelada")
