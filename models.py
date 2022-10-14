# python imports
from datetime import date, datetime
from uuid import UUID
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field, EmailStr


class UserId(BaseModel):
    user_id: UUID = Field(...)  # Universal Unique Identifier


class UserBase(UserId):
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
        min_length=8,
        max_length=64
    )


class UserRegister(User, UserLogin):
    pass


class TweetPost(BaseModel):
    content: str = Field(..., min_length=1, max_length=256)
    by: UserId = Field(...)


class Tweet(TweetPost):
    tweet_id: UUID = Field(...)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field()
