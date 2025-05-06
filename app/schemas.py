from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # was orm_mode=True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True  # was orm_mode=True


class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        from_attributes = True  # was orm_mode=True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    # At 7:32:41 you may run into internal server error, to fix this you need to change 'str' to 'int '  in TokenData schema.

class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]
