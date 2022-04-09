import string
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Text
from drivers.DBconnection import meta, engine

Register_user = Table(
    "informacion_basica", meta,
    Column("id", Integer, primary_key=True),
    Column("productos", String(255)),
    Column("precios", Integer),
   )

meta.create_all(engine)
