from fastapi import APIRouter
from usesCase.registro import getandsaveRegisters,updateUserRegister,createUserRegister
from domains.schemas.registro import informacion_basica


registro=APIRouter()

@registro.post("/crear nuevo producto/")
async def get_create_register(user : informacion_basica):
    infoUser = createUserRegister(user)
    return infoUser

@registro.get("/mostrar productos")
async def get_users_register(user : informacion_basica):
    infoUser = getandsaveRegisters(user)
    return infoUser

@registro.put("/actualizar productos")
async def get_users_actualizar(user: informacion_basica):
    infoUser = updateUserRegister(user)
    return infoUser








