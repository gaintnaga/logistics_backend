from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import schemas,models
from app.database import get_db
from passlib.context import CryptContext
from app.security import create_access_token,get_current_admin_user
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


pwd_context= CryptContext(schemes=['bcrypt'],deprecated="auto")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

# register route and logic

@router.post("/register")
def register(user:schemas.UserCreate,db: Session = Depends(get_db),current_user: dict = Depends(get_current_admin_user)):
    
    #check existing user
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    #hash password
    hashed_password = pwd_context.hash(user.password)

    new_user = models.User(
        name = user.name,
        email = user.email,
        phone_number = user.phone_number,
        password = hashed_password,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# login route and logic


@router.post("/login")
def login(request: schemas.LoginRequest,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400,detail="Invalid Email or Password")
    
    if not verify_password(request.password,user.password):
        raise HTTPException(status_code=400,detail="Invalid Email or Password")
    
    token_data = {"sub":user.email,"id":user.id}
    access_token = create_access_token(token_data)

    return {"access_token":access_token, "token_type":"bearer"}
    