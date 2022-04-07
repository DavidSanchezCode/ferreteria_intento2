import json
from fastapi import FastAPI
from domains.schemas.registro import informacion_basica
from cryptography.fernet import Fernet
from domains.service import registro


key = Fernet.generate_key()
f = Fernet(key)
app = FastAPI()


def getandsaveRegisters(user: informacion_basica):
    new_user = {"nombres": user.nombres,
                "apellidos": user.apellidos,
                "correo": user.correo,
                "telefono": user.telefono,
                "edad": user.edad
                }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    registro.getandsaveRegisters(new_user)


def createUserRegister(user: informacion_basica):
    new_user = {
        "nombres": user.nombres,
        "apellidos": user.apellidos,
        "correo": user.correo,
        "telefono": user.telefono,
        "edad": user.edad
    }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    registro.createUserRegister(new_user)


def updateUserRegister(user: informacion_basica):
    new_user = {
        "nombres": user.nombres,
        "apellidos": user.apellidos,
        "correo": user.correo,
        "telefono": user.telefono,
        "edad": user.edad
    }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    registro.updateUserRegister(new_user)


def selectUserlogin(user: informacion_basica):
    try:
        login_user = {
            "correo": user.correo,
            "password": user.password
        }
        login_user["password"] = f.decrypt(token=f, ttl=None)

    except ValueError:
        print(ValueError)
        print(
            "ERROR: [useCases:users] - Error ocurred in find and save user information")

    return registro.selectUserlogin(login_user)
