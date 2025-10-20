from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "your_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRED = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data:dict,expires_delta:int=ACCESS_TOKEN_EXPIRED):
    to_encode= data.copy()
    expire = datetime.utcnow()+timedelta(minutes=expires_delta)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_token(token:str):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"www-Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        user_id:str = payload.get("id")

        if email is None or user_id is None:
            raise credential_exception
        return{"email":email,"id":user_id}
    except JWTError:
        raise credential_exception
    
def get_current_user(token:str = Depends(oauth2_scheme)):
    return verify_token(token)    

def get_current_admin_user(current_user:dict = Depends(get_current_user)):
    if current_user['role'] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Admin privilages required")
    return current_user       
