from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from chat.database import get_session
from chat.models import Message

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("/")
def list_messages(db: Session = Depends(get_session)):
    return db.query(Message).all()

@router.get("/room/{room_id}")
def messages_by_room(room_id: int, db: Session = Depends(get_session)):
    return db.query(Message).filter(Message.room_id == room_id).all()
