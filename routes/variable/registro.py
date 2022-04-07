from fastapi import APIRouter
from usesCase.registro import getandsaveRegisters,updateUserRegister,selectUserlogin,createUserRegister
from domains.schemas.registro import informacion_basica
from domains.schemas.login import informacion_login

registro=APIRouter()

@registro.post("/registro/")
async def get_create_register(user : informacion_basica):
    infoUser = createUserRegister(user)
    return infoUser

@registro.get("/registro/{nombre}")
async def get_users_register(user : informacion_basica):
    infoUser = getandsaveRegisters(user)
    return infoUser

@registro.put("/registro/{nombre}")
async def get_users_actualizar(user: informacion_basica):
    infoUser = updateUserRegister(user)
    return infoUser

@registro.get("/login/{password}")
async def  get_password_user(user : informacion_login):
    infoUser = selectUserlogin(user)
    return infoUser






