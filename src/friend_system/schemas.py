from pydantic import BaseModel
from src.auth.schemas import UserRead


class Friend(BaseModel):
    user_id: int
    friend_id: int


class FriendResponseModel(BaseModel):
    user: UserRead
    friend: UserRead

    class Config:
        from_attributes = True


