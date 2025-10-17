from pydantic import BaseModel
from typing import Optional

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