import pymysql

class Horario():
    id = ''
    turno = ''
    hora_inicio = ''
    hora_final = ''

    def __init__(self, datos) -> None:
        self.id, self.turno, self.hora_inicio, self.hora_final = (
            lambda d: list(map(lambda x: x if x not in ('', None) else '', d)))(datos)

def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    return conn

def post_horario(turno, hora_inicio, hora_final):
    bd = conectar_bd()
    consulta = "INSERT INTO control_escolar.horario (turno, hora_inicio, hora_final) VALUES (%s,%s,%s)"
    cur = bd.cursor()
    cur.execute(consulta, (turno, hora_inicio, hora_final))
    bd.commit()
    bd.close()

def get_horario(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM horario WHERE id = %s"
    cur = bd.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    bd.close()
    return output[0]

def update_horario(id, horario):
    bd = conectar_bd()
    consulta = "UPDATE horario SET turno = %s, hora_inicio = %s, hora_final = %s WHERE id = %s"
    cur = bd.cursor()
    cur.execute(consulta, (horario.turno, horario.hora_inicio, horario.hora_final, id))
    bd.commit()
    bd.close()


def delete_horario(id):
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("DELETE FROM horario WHERE id = %s", id)
    bd.commit()
    bd.close()

def get_max_id():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT MAX(id) FROM horario")
    output = cur.fetchall()
    bd.close()
    return output[0]

def get_horario(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM horario WHERE id = %s"
    cur = bd.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    bd.close()

    if output:
        return output[0]  # Si hay resultados, devuelve el primer elemento
    else:
        return None  # Si no hay resultados, devuelve None o un valor que indique la ausencia de datos
