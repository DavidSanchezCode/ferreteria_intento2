from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Text
from drivers.DBconnection import meta,engine

Register_user = Table(
    "informacion_basica",meta,
    Column("id", Integer,primary_key=True),
    Column("nombres",String(255)),
    Column("apellidos",String(255)),
    Column("correo",String(255)),
    Column("telefono",Integer(255)),
    Column("edad",Integer)
    )

meta.create_all(engine)




