import pymysql
class Perfil:
    def __init__(self, raw_pefil) :
        self.id ,self.nombre = raw_pefil
    def __str__(self) -> str:
        return self.nombre
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

def get_pefiles():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("select * from perfiles")
    output = cur.fetchall()
    salida = []
    for x in output:
        salida.append(Perfil(x))
    return salida
get_pefiles()