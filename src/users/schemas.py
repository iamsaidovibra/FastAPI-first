import uuid

from pydantic import BaseModel, EmailStr
from datetime import datetime 


class User(BaseModel):
    uid: uuid.UUID
    email: EmailStr
    phone_num: str
    front_photo: str
    back_photo: str
    selfie_photo: str
    password: str
    fio: str
    gender: bool #True = male, False = female
    birth_date: str
    created_at: datetime
    updated_at: datetime


class UserCreateModel(BaseModel):
    email: EmailStr
    phone_num: str
    password: str
    fio: str
    gender: bool
    birth_date: str


class UserUpdateModel(BaseModel):
    email: EmailStr
    phone_num: str
    password: str



