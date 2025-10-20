from fastapi import APIRouter,Depends,HTTPException
from app.security import get_current_user,get_current_admin_user
from sqlalchemy.orm import Session
from app import models,schemas
from app.database import get_db
from passlib.context import CryptContext
from app.utils.email_sender import send_rider_email
import random, string

router = APIRouter(
    prefix="/riders",
    tags=['Riders']
)

pwd_context= CryptContext(schemes=['bcrypt'],deprecated="auto")

def generate_password(length)
@router.get("/")
def get_all_riders(db : Session = Depends(get_db), current_admin: dict = Depends(get_current_admin_user)):
    new_riders = models.User(
        name = "Rider name",
        email = "rider@email.com",
        password = pwd_context.hash("rider_password"),
        role = "rider"
    )
    db.add(new_riders)
    db.commit()
    db.refresh(new_riders)

    send_rider_email(new_riders.name, new_riders.email, password)

    return {"message": f"Rider {new_riders.email} created successfully"}