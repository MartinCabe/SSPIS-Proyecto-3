import pymysql

def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    return conn

def buscar_usuario(id):
    db = conectar_bd()
    consulta = "SELECT nombre, apellido_paterno, apellido_materno, correo FROM usuarios WHERE id = %s AND perfil = 3 AND estado = 'ACTIVO'"
    cur = db.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    db.close()
    return output[0]

def buscar_alumno(id):
    try:
        db = conectar_bd()
        consulta = "SELECT estado, fecha_nacimiento, carrera FROM alumnos WHERE id = %s"
        cur = db.cursor()
        cur.execute(consulta, id)
        output = cur.fetchall()
        db.close()
        return output[0]
    except IndexError:
        return ()

def get_carreras():
    db = conectar_bd()
    consulta = "SELECT id, nombre FROM carreras"
    cur = db.cursor()
    cur.execute(consulta)
    output = cur.fetchall()
    db.close()
    return output

def get_materias_disponibles(id):
    db = conectar_bd()
    consulta = "SELECT m.id AS id_materia, m.asignatura AS nombre_materia FROM materias m WHERE m.carrera = (SELECT a.carrera FROM alumnos a WHERE a.id = %s) AND NOT EXISTS (SELECT 1 FROM alumno_materia am WHERE am.id_alumno = %s AND am.id_materia = m.id) AND m.estado = 'ACTIVO'"
    cur = db.cursor()
    cur.execute(consulta, (id, id))
    output = cur.fetchall()
    db.close()
    return output

def get_materias_registradas(id):
    db = conectar_bd()
    consulta = "SELECT m.id AS id_materia, m.asignatura AS nombre_materia FROM materias m JOIN alumno_materia am ON m.id = am.id_materia WHERE am.id_alumno = %s"
    cur = db.cursor()
    cur.execute(consulta, id)
    output = cur.fetchall()
    db.close()
    return output

def limpiar_materias(id):
    # La opcion nuclear siono *emoji del pulgar arriba*
    db = conectar_bd()
    consulta = "DELETE FROM alumno_materia WHERE id_alumno = %s"
    cur = db.cursor()
    cur.execute(consulta, id)
    db.commit()
    db.close()

def registrar_materia(id_alumno, id_materia):
    db = conectar_bd()
    consulta = "INSERT INTO alumno_materia (id_alumno, id_materia) VALUES (%s, %s)"
    cur = db.cursor()
    cur.execute(consulta, (id_alumno, id_materia))
    db.commit()
    db.close()

def get_materias_carrera(id_carrera):
    db = conectar_bd()
    consulta = "SELECT m.id AS id_materia, m.asignatura AS nombre_materia FROM materias m JOIN carreras c ON m.carrera = c.id WHERE c.id = %s"
    cur = db.cursor()
    cur.execute(consulta, id_carrera)
    output = cur.fetchall()
    db.close()
    return output

def registrar_alumno(id, estado, nacimiento, carrera):
    db = conectar_bd()
    consulta = "INSERT INTO alumnos (id, estado, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
    cur = db.cursor()
    cur.execute(consulta, (id, estado, nacimiento, carrera))
    db.commit()
    db.close()

def editar_alumno(id, estado, nacimiento, carrera):
    db = conectar_bd()
    consulta = "UPDATE alumnos SET estado = %s, fecha_nacimiento = %s, carrera = %s WHERE id = %s"
    cur = db.cursor()
    cur.execute(consulta, (estado, nacimiento, carrera, id))
    db.commit()
    db.close()
