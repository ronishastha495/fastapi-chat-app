from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from chat.database import get_session
from chat.models import Room
from chat.schemas import RoomCreate, RoomResponse

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.post("/", response_model=RoomResponse)
def create_room(room: RoomCreate, db: Session = Depends(get_session)):
    existing = db.query(Room).filter(Room.name == room.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Room already exists")
    new_room = Room(**room.dict())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room  # ✅ Now FastAPI can serialize this using `orm_mode`
