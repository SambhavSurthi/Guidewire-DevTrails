from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    phone: str
    password: str
    full_name: str
    role: str = "worker"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class LoginResponse(Token):
    user: UserResponse
    worker_profile: Optional[dict] = None

class RegisterResponse(Token):
    user_id: str
    email: str
    role: str
