from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    soc_dem_profile_id: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    soc_dem_profile_id: int | None = None


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
