from drivers.DBconnection import conn
from domains.models.registro import Register_user
from domains.schemas.registro import informacion_basica

def getUserRegister(id):
    return conn.execute(Register_user.select().where(Register_user.c.id== id)).first()

def createUserRegister(user: informacion_basica):
    return conn.execute(Register_user.insert().values(user))

def updateUserRegister(user: informacion_basica, UsuarioId):
    return conn.execute(Register_user.update().values(user).where (Register_user.c.id== UsuarioId))