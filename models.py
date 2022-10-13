# python imports
from datetime import date
from uuid import UUID
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    user_id: UUID = Field(...)  # Universal Unique Identifier
    email: EmailStr = Field(...)


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
    )


class Tweet(BaseModel):
    pass
