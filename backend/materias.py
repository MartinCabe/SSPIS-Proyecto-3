import pymysql

class Materia():
    id=''
    asignatura=''
    semestre=''
    creditos=''
    carrera = ''
    estado = ''
    def __init__(self,datos) -> None:
        self.id,self.asignatura,self.semestre,self.creditos, self.carrera, self.estado \
            = (lambda d: list(map(lambda x: x if x not in ('', None) else '', d)))(datos)

def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    return conn

def post_materia(asignatura, semestre, creditos, carrera):
    bd = conectar_bd()
    consulta = "INSERT INTO control_escolar.materias (asignatura, semestre, creditos, carrera) VALUES (%s,%s,%s,%s)"
    cur = bd.cursor()
    cur.execute(consulta,(asignatura, semestre, creditos, carrera))
    bd.commit()   
    bd.close()

def get_materia(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM materias WHERE id = %s AND estado = 'ACTIVO'"
    cur = bd.cursor()
    cur.execute(consulta,id)
    output = cur.fetchall()
    bd.close()
    return output[0]

def update_materia(id,materia):
    bd = conectar_bd()
    consulta = "UPDATE materias SET asignatura = %s , semestre=%s, creditos = %s, carrera = %s WHERE id=%s"
    cur = bd.cursor()
    cur.execute(consulta,(materia.asignatura, materia.semestre, materia.creditos,materia.carrera,id))
    bd.commit()
    bd.close()

def delete_materia(id):
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("UPDATE materias SET estado = 'ELIMINADO' WHERE id = %s",id)
    bd.commit()
    bd.close()

def get_max_id():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT MAX(id) FROM materias")
    output = cur.fetchall()
    bd.close()
    return output[0]

def get_nombres_carreras():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT id, nombre FROM carreras")
    output = cur.fetchall()
    bd.close()
    return output