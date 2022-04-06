import json
from fastapi import FastAPI
from domains.schemas.registro import informacion_basica

app = FastAPI()

@app.post("/registro")
def getandsaveRegisters(user: informacion_basica):
                       {"nombre":user.nombres,
                        "apellidos":user.apellidos,
                        "correo":user.correo,
                        "telefono":user.telefono,
                        "edad":user.edad }
    
    


