import pymysql


class Usuario():
    id=''
    perfil=''
    nombre=''
    apellido_paterno=''
    apellido_materno=''
    correo=''
    contraseña=''
    nombre_usuario=''
    estado=''
    def __init__(self,datos) -> None:
        self.id,self.perfil,self.nombre,self.apellido_paterno,self.apellido_materno,self.correo,self.contraseña,self.nombre_usuario,self.estado \
            = (lambda d: list(map(lambda x: x if x not in ('', None) else '', d)))(datos)


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

def post_usuario(perfil,nombre,ap_paterno,ap_materno,correo,contraseña,nombre_usuario):
    bd = conectar_bd()
    consulta = "INSERT INTO control_escolar.usuarios (perfil,nombre,apellido_paterno,apellido_materno,correo,contraseña,nombre_usuario) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cur = bd.cursor()
    cur.execute(consulta,(perfil,nombre,ap_paterno,ap_materno,correo,contraseña,nombre_usuario))
    bd.commit()     
    bd.close()

def get_usuarios():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("select * from usuarios")
    output = cur.fetchall()
    print(type(output))
    print(output[0])
    usuario = Usuario(output[0])
    print(usuario.nombre,usuario.contraseña)
    bd.close()

def get_usuario(id):
    bd = conectar_bd()
    consulta = "SELECT * FROM usuarios WHERE id = %s AND estado = 'ACTIVO'"
    cur = bd.cursor()
    cur.execute(consulta,id)
    output = cur.fetchall()
    bd.close()
    return output[0]

def update_usuario(id,usuario):
    bd = conectar_bd()
    consulta = "UPDATE usuarios SET perfil = %s , nombre=%s, apellido_paterno = %s, apellido_materno = %s, correo = %s, contraseña = %s, nombre_usuario=%s, estado='ACTIVO' WHERE id=%s"
    cur = bd.cursor()
    cur.execute(consulta,(usuario.perfil,usuario.nombre,usuario.apellido_paterno,usuario.apellido_materno,usuario.correo,usuario.contraseña, usuario.nombre_usuario,id))
    bd.commit()
    bd.close()

def delete_usuario(id):
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("UPDATE usuarios SET estado = 'ELIMINADO' WHERE id = %s",id)
    bd.commit()
    bd.close()

def get_max_id():
    bd = conectar_bd()
    cur = bd.cursor()
    cur.execute("SELECT MAX(id) FROM usuarios")
    output = cur.fetchall()
    bd.close()
    return output[0]