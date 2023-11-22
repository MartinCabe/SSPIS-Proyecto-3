import pymysql

class Maestro():
    id=''
    nombre=''
    apellido_paterno=''
    apellido_materno=''
    correo=''
    carrera = ''
    materia = ''
    grado_de_estudio = ''
    estado = ''
    def __init__(self,datos) -> None:
        self.id,self.nombre,self.apellido_paterno,self.apellido_materno,self.correo, self.carrera,self.materia,self.grado_de_estudio ,self.estado \
            = (lambda d: list(map(lambda x: x if x not in ('', None) else '', d)))(datos)

def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    return conn

def get_nombres_carreras():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT id, nombre FROM carreras")
    output = cur.fetchall()
    bd.close()
    return output

def get_nombres_materias():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT id, asignatura FROM materias")
    output = cur.fetchall()
    bd.close()
    return output

def post_maestro(nombre, ap_paterno, ap_materno, correo, carrera, materia, grado_de_estudio):
    bd = conectar_bd()
    consulta = "INSERT INTO maestros (nombre, apellido_paterno, apellido_materno, correo, carrera, materia, grado_de_estudio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur = bd.cursor()
    cur.execute(consulta, (nombre, ap_paterno, ap_materno, correo, carrera, materia, grado_de_estudio))
    bd.commit()
    bd.close()

def get_maestros():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT * FROM maestro")
    output = cur.fetchall()
    maestros = [Maestro(datos) for datos in output]
    bd.close()
    return maestros

def get_maestro(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM maestros WHERE id = %s AND estado = 'ACTIVO'"
    cur = bd.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    bd.close()
    if output:
        return output[0]
    return None

def update_maestro(id, maestro):
    bd = conectar_bd()
    consulta = "UPDATE maestros SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, correo = %s, carrera = %s, materia = %s, grado_de_estudio = %s WHERE id = %s"
    cur = bd.cursor()
    cur.execute(consulta, (maestro.nombre, maestro.apellido_paterno, maestro.apellido_materno, maestro.correo, maestro.carrera, maestro.materia, maestro.grado_de_estudio, id))
    bd.commit()
    bd.close()

def delete_maestro(id):
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("UPDATE maestros SET estado = 'ELIMINADO' WHERE id = %s", id)
    bd.commit()
    bd.close()

def get_max_id():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT MAX(id) FROM maestros")
    output = cur.fetchall()
    print(output)
    if output[0][0] is None:
        output = ((0,0),(0))
    else:
        print("cola")
    bd.close()
    return output[0]
