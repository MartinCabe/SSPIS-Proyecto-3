import pymysql

class Carreras():
    id = ''
    nombre = ''
    semestres = ''
    estado = ''

    def __init__(self,datos) -> None:
        self.id,self.nombre,self.semestres, self.estado \
            = (lambda d: list(map(lambda x: x if x not in ('', None) else '', d)))(datos)

def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    return conn

def get_max_id():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT MAX(id) FROM carreras")
    output = cur.fetchall()
    bd.close()
    return output[0]

def post_carrera(nombre, semestres):
    bd = conectar_bd()
    consulta = "INSERT INTO control_escolar.carreras (nombre, numero_semestres) VALUES(%s, %s)"
    cur = bd.cursor()
    cur.execute(consulta, (nombre, semestres))
    bd.commit()
    bd.close()

def get_carrera(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM carreras WHERE id = %s AND estado = 'ACTIVO'"
    cur = bd.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    bd.close()
    return output[0]

def update_carrera(id, carrera):
    bd = conectar_bd()
    consulta = "UPDATE carreras SET nombre = %s, numero_semestres = %s WHERE id = %s"
    cur = bd.cursor()
    cur.execute(consulta,(carrera.nombre, carrera.semestres, id))
    bd.commit()
    bd.close()

def delete_carrera(id):
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("UPDATE carreras SET estado = 'ELIMINADO' WHERE id = %s",id)
    bd.commit()
    bd.close()