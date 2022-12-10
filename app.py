from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="Approval API",
    description="Esta API es para aceptar o rechazar dar un crédito a una persona"
    )
app.include_router(user)