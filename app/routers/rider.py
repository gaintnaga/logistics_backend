from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,database

router = APIRouter(
    prefix="/riders",
    tags=['Riders']
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()    

@router.post("/",response_model=schemas.RiderResponse)
def create_rider(rider:schemas.RiderCreate,db:Session=Depends(get_db)):
    new_rider = models.Rider(name = rider.name,latitude=rider.latitude,longitude=rider.longitude)
    db.add(new_rider)
    db.commit()
    db.refresh(new_rider)
    return new_rider