from pydantic import BaseModel 

class informacion_basica(BaseModel):
    id:str
    nombres:str
    apellidos:str
    correo:str
    telefono:str
    edad:str
    password:str