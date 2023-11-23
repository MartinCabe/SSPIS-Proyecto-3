import tkinter as tk
from tkinter import ttk
import pymysql
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Planeacion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = None
        self.scrollbar = None

        # Botón para mostrar la información de los grupos
        self.btn_mostrar_grupos = tk.Button(self, text="Mostrar Grupos", command=self.mostrar_grupos)
        self.btn_mostrar_grupos.pack()

    def mostrar_grupos(self):
        # Destruir el canvas y la barra de desplazamiento si ya existen
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.scrollbar.destroy()

        # Conexión a la base de datos
        mydb = pymysql.connect(
            host='localhost',
            user='root',
            passwd='admin',
            db='control_escolar'
        )

        # Cursor para ejecutar consultas SQL
        cursor = mydb.cursor()

        # Consulta para obtener los datos de los grupos con nombres relacionados
        query = """
        SELECT g.nombre_grupo, s.nombre_salon, m.asignatura, ma.nombre, h.hora_inicio, h.hora_final
        FROM grupos g
        INNER JOIN salones s ON g.salon = s.id
        INNER JOIN materias m ON g.materia = m.id
        INNER JOIN maestros ma ON g.maestro = ma.id
        INNER JOIN horario h ON g.horario = h.id
        ORDER BY g.id
        """

        cursor.execute(query)
        grupos = cursor.fetchall()

        # Crear tabla para mostrar la información de los grupos con Matplotlib
        headers = ['Grupo', 'Salón', 'Materia', 'Maestro', 'Hora Inicio', 'Hora Final']
        data = [[grupo[i] for i in range(len(grupo))] for grupo in grupos]

        fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño de la tabla

        ax.axis('off')  # Ocultar ejes

        table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center', colColours=['skyblue'] * len(headers))
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 2)

        # Crear canvas para la tabla y agregar barras de desplazamiento
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Ajustar la ubicación del canvas

        # Agregar barra de desplazamiento a la izquierda
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas_widget.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_widget.configure(yscrollcommand=self.scrollbar.set)

        # Cerrar el cursor y la conexión
        cursor.close()
        mydb.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Ajustar el tamaño de la ventana

    planeacion_tab = Planeacion(root)
    planeacion_tab.pack(fill=tk.BOTH, expand=True)  # Expandir el Frame

    root.mainloop()
