from pydantic import BaseModel 

class informacion_login(BaseModel):
    id:str
    correo:str
    password:str