from pydantic import BaseModel,EmailStr
from typing import Optional

class UserBase(BaseModel):
    name:str
    email:EmailStr
    phone_number:str
    role:Optional[str]="user"        

class UserCreate(UserBase):
    password:str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RiderBase(BaseModel):
    name: str
    latitude:float
    longitude:float

class RiderCreate(RiderBase):
    pass

class RiderUpdate(BaseModel):
    latitude:float
    longitude:float

class RiderResponse(RiderBase):
    id:int

    class Config:
        orm_mode = True    