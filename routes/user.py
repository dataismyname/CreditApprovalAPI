from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
from sqlalchemy import select

user = APIRouter()


@user.get("/users", tags=["Clientes"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users", tags=["Clientes"])
def add_user(user: User):
    new_user = {'PRIMER_NOMBRE': user.PRIMER_NOMBRE,  'APELLIDO_PAT': user.APELLIDO_PAT, 'APELLIDO_MAT': user.APELLIDO_MAT,
    'FECHA_NAC': user.FECHA_NAC, 'INGRESOS_MENSUALES': user.INGRESOS_MENSUALES, 'DEPENDIENTES': user.DEPENDIENTES}
    new_user['RFC'] = (user.APELLIDO_PAT[0:2]).upper() + user.APELLIDO_MAT[0:1].upper() + user.PRIMER_NOMBRE[0:1] + user.FECHA_NAC[8:] + user.FECHA_NAC[3:5] + user.FECHA_NAC[0:2]
    if user.INGRESOS_MENSUALES > 25000:
        new_user['APROBADO'] = 'APROBADO'
    elif user.INGRESOS_MENSUALES > 15000 and user.DEPENDIENTES < 3:
        new_user['APROBADO'] = 'APROBADO'
    else:
        new_user['APROBADO'] = 'RECHAZADO'

    result = conn.execute(users.insert().values(new_user))
    fin = conn.execute(select([users.c.ID, users.c.RFC, users.c.APROBADO]).where(users.c.ID == result.lastrowid)).fetchone()
    return fin