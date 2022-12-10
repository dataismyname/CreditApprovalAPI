from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table('users', meta, 
        Column('ID', Integer, primary_key=True),
        Column('PRIMER_NOMBRE', String(255)),
        Column('APELLIDO_PAT', String(255)),
        Column('APELLIDO_MAT', String(255)),
        Column('FECHA_NAC', String(255)),
        Column('RFC', String(255)),
        Column('INGRESOS_MENSUALES', Integer),
        Column('DEPENDIENTES', Integer),
        Column('APROBADO', String(255)))

meta.create_all(engine)
