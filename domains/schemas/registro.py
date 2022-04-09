from pydantic import BaseModel 

class informacion_basica(BaseModel):
    id:str
    productos:str
    precios:int
  