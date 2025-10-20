from fastapi import FastAPI
from .routers import rider,auth
from . import models,database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Delivery Tracking System")

app.include_router(auth.router)
app.include_router(rider.router)

@app.get("/")
def test():
    return {"messsage":"Hello World"}

