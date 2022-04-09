import json
from fastapi import FastAPI
from domains.schemas.registro import informacion_basica
from cryptography.fernet import Fernet
from domains.service import registro


key = Fernet.generate_key()
f = Fernet(key)
app = FastAPI()


def getandsaveRegisters(user: informacion_basica):
    new_user = {
        "productos": user.productos,
        "precios": user.precios
    }

    registro.getandsaveRegisters(new_user)


def createUserRegister(user: informacion_basica):
    new_user = {
        "productos": user.productos,
        "precios": user.precios
    }

    registro.createUserRegister(new_user)


def updateUserRegister(user: informacion_basica):
    new_user = {
        "productos": user.productos,
        "precios": user.precios
    }

    registro.updateUserRegister(new_user)
