from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, date
import uuid


class User(SQLModel, table=True):
    __tablename__  = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    email: str
    phone_num: str
    front_photo: str
    back_photo: str
    selfie_photo: str
    password: str
    fio: str
    gender: bool
    birth_date: date
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


def __repr__(self):
    return f"<User {self.email}>"


    

