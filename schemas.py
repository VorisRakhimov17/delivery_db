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

class Setting(BaseModel):
    authjwt_secret_key: str = "baa95a831f1988bcd6667f3edb472010697b6a99dd4103cfc469984a0f21c1db"

class LoginModel(BaseModel):
    username_or_email: str
    password: str


