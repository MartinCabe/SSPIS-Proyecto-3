import pymysql
from backend.usuarios import Usuario
def conectar_bd():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='control_escolar'
    )
    # cur = conn.cursor()
    # cur.execute("select * from alumnos")
    # output = cur.fetchall()
    # print(output)
    # conn.close()
    return conn


def logear_usuario(nombre_usuario,contraseña):
    bd = conectar_bd()
    consulta = "SELECT * from usuarios where nombre_usuario = %s AND contraseña = %s"
    cur = bd.cursor()
    cur.execute(consulta,(nombre_usuario,contraseña))
    output = cur.fetchall()
    usuario_logeado = Usuario(output[0])
    print(usuario_logeado)
    bd.close()
    return usuario_logeado

