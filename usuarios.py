import tkinter as tk
import re
from tkinter import ttk,END, messagebox, simpledialog
from backend.pefil import get_pefiles
from backend.usuarios import post_usuario,get_usuario,update_usuario,delete_usuario,Usuario, get_max_id

def validar_cadena(cadena):
    if re.match('^[a-zA-Z\s]+$', cadena):
        return cadena
    else:
        raise ValueError("Cadena tiene caracteres invalidos")

def validar_email(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return email
    else:
        raise ValueError("Email no valido")

def validar_lenght(cadena):
    if len(cadena) >= 4:
        return cadena
    else:
        raise ValueError("Cadena con menos de 4 caracteres")

class Usuarios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # ----- WIDGETS -----
        # Labels
        tk.Label(self, text = "Ingrese codigo de usuario:").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "ID:").grid(row = 1, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre:").grid(row = 2, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Paterno:").grid(row = 3, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "A Materno:").grid(row = 4, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "E-Mail:").grid(row = 5, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "Nombre Usuario:").grid(row = 1, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Password:").grid(row = 2, column = 2, padx = 10, pady = 10)
        tk.Label(self, text = "Perfil:").grid(row = 3, column = 2, padx = 10, pady = 10)

        # Entries
        self.entry_usuarios_buscar = tk.Entry(self)
        self.entry_usuarios_id = tk.Entry(self)
        self.entry_usuarios_nombre = tk.Entry(self)
        self.entry_usuarios_paterno = tk.Entry(self)
        self.entry_usuarios_materno = tk.Entry(self)
        self.entry_usuarios_email = tk.Entry(self)
        self.entry_usuarios_username = tk.Entry(self)
        self.entry_usuarios_password = tk.Entry(self)
        self.entry_usuarios_buscar.grid(row=0, column=1, padx=10, pady=10)
        self.entry_usuarios_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_usuarios_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.entry_usuarios_paterno.grid(row=3, column=1, padx=10, pady=10)
        self.entry_usuarios_materno.grid(row=4, column=1, padx=10, pady=10)
        self.entry_usuarios_email.grid(row=5, column=1, padx=10, pady=10)
        self.entry_usuarios_username.grid(row=1, column=3, padx=10, pady=10)
        self.entry_usuarios_password.grid(row=2, column=3, padx=10, pady=10)

        # ComboBox
        self.perfiles = get_pefiles()
        self.combo_usuarios_perfil = ttk.Combobox(self)
        self.combo_usuarios_perfil.grid(row = 3, column = 3, padx = 10, pady = 10)
        self.combo_usuarios_perfil.config(values=self.perfiles)
        # Buttons
        self.button_usuarios_buscar = tk.Button(self, text = "Buscar", command=lambda:self.buscar_usuario())
        self.button_usuarios_nuevo = tk.Button(self, text = "Nuevo", command = lambda:self.nuevo_usuario())
        self.button_usuarios_guardar = tk.Button(self, text = "Guardar", command=lambda:self.guardar_usuario())
        self.button_usuarios_cancelar = tk.Button(self, text = "Cancelar", command=lambda:self.limpiar_campos())
        self.button_usuarios_editar = tk.Button(self, text = "Editar")
        self.button_usuarios_baja = tk.Button(self, text = "Baja")
        self.button_usuarios_buscar.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.button_usuarios_nuevo.grid(row = 6, column = 0, padx = 10, pady = 10)
        self.button_usuarios_guardar.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.button_usuarios_cancelar.grid(row = 6, column = 2, padx = 10, pady = 10)
        self.button_usuarios_editar.grid(row = 6, column = 3, padx = 10, pady = 10)
        self.button_usuarios_baja.grid(row = 6, column = 4, padx = 10, pady = 10)

        self.entry_usuarios_id.config(state = "disabled")

    def nuevo_usuario(self):
        self.limpiar_campos()
        self.entry_usuarios_id.config(state = "normal")
        self.entry_usuarios_id.insert(0, int(get_max_id()[0]) + 1)
        self.entry_usuarios_id.config(state = "disabled")

    def representar_perfil(self,seleccion):
        for x in self.perfiles:
            if seleccion == x.nombre:
                return x.id
        return None
    
    def guardar_usuario(self):
        try:
            post_usuario(
                self.representar_perfil(self.combo_usuarios_perfil.get()),
                validar_cadena(self.entry_usuarios_nombre.get()),
                validar_cadena(self.entry_usuarios_paterno.get()),
                validar_cadena(self.entry_usuarios_materno.get()),
                validar_email(self.entry_usuarios_email.get()),
                validar_lenght(self.entry_usuarios_password.get()),
                validar_lenght(self.entry_usuarios_username.get()),
            )
            messagebox.showinfo(title = "Aviso", message = "Usuario guardado con exito")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")
        
    def colocar_datos_en_entrys(self,usuario):
        self.entry_usuarios_id.config(state = "normal")
        self.entry_usuarios_id.insert(0, usuario.id)
        self.entry_usuarios_id.config(state = "disabled")
        self.entry_usuarios_nombre.insert(0, usuario.nombre)
        self.entry_usuarios_paterno.insert(0, usuario.apellido_paterno)
        self.entry_usuarios_materno.insert(0, usuario.apellido_materno)
        self.entry_usuarios_email.insert(0, usuario.correo)
        self.entry_usuarios_username.insert(0, usuario.nombre_usuario)
        self.entry_usuarios_password.insert(0, usuario.contraseña)
        self.combo_usuarios_perfil.insert(0,usuario.perfil)
    
    def limpiar_campos(self):
        self.entry_usuarios_id.config(state = "normal")
        self.entry_usuarios_id.delete(0,END)
        self.entry_usuarios_id.config(state = "disabled")
        self.entry_usuarios_nombre.delete(0,END)
        self.entry_usuarios_paterno.delete(0,END)
        self.entry_usuarios_materno.delete(0,END)
        self.entry_usuarios_email.delete(0,END)
        self.entry_usuarios_username.delete(0,END)
        self.entry_usuarios_password.delete(0,END)
        self.combo_usuarios_perfil.delete(0,END)

    def editar_usuario(self,id):
        try:
            usuario =Usuario((id,self.representar_perfil(self.combo_usuarios_perfil.get()),
                validar_cadena(self.entry_usuarios_nombre.get()),
                validar_cadena(self.entry_usuarios_paterno.get()),
                validar_cadena(self.entry_usuarios_materno.get()),
                validar_email(self.entry_usuarios_email.get()),
                validar_lenght(self.entry_usuarios_password.get()),
                validar_lenght(self.entry_usuarios_username.get()),
                'ACTIVO')) 
            update_usuario(id,usuario)
            messagebox.showinfo(title = "Aviso", message = "Usuario editado con exito")
            self.limpiar_campos()
        except:
            messagebox.showerror(title = "Error", message = "Datos invalidos o incompletos")
        

    def borrar_usuario(self,id):
        confirmar = messagebox.askyesno(title = "Confirmacion", message = f"¿Estás seguro de eliminar al usuario con el id: {id} ?")
        if confirmar:
            delete_usuario(id)
            messagebox.showinfo(title = "Aviso", message = "Usuario eliminado con exito")
            self.limpiar_campos()
        else:
            messagebox.showerror(title = "Error", message = "Operacion cancelada")

    def buscar_usuario(self):
        try:
            usuario = Usuario(get_usuario(int(self.entry_usuarios_buscar.get())))
            self.limpiar_campos()
            self.colocar_datos_en_entrys(usuario)
            self.button_usuarios_editar.config(command=lambda:self.editar_usuario(usuario.id))
            self.button_usuarios_baja.config(command=lambda:self.borrar_usuario(usuario.id))
        except:
            messagebox.showerror(title = "Error", message = "Dato de busqueda invalido")