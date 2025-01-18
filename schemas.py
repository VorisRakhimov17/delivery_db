
from pydantic import BaseModel
from typing import Optional



class SignUpModel(BaseModel):
    id: Optional[int]  = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "VorisRakhimov",
                "email": "VorisRakhimov17@gmail.com",
                "password": "admin12345",
                "is_staff": False,
                "is_active": True
            }
        }