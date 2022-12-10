from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    PRIMER_NOMBRE: str
    APELLIDO_PAT: str
    APELLIDO_MAT: str
    FECHA_NAC: str
    INGRESOS_MENSUALES: int
    DEPENDIENTES: int