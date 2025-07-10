# chat/schemas.py

from pydantic import BaseModel
from typing import Optional

class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None

class RoomResponse(RoomCreate):
    id: int

    class Config:
        orm_mode = True
