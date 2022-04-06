from fastapi import APIRouter
from usesCase.registro import getandsaveRegisters

registro=APIRouter()

@registro.get("/registro/{username}")
async def get_users_register(username):
    infoUser = getandsaveRegisters(username)
    return infoUser



