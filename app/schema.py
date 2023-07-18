from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserOut(BaseModel):
    id: int
    email: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    created_at: datetime
    id: int
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
