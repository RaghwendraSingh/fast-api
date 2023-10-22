from fastapi import APIRouter, Response, status, Depends, Body
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas import UserBase, UserDisplay
from db import db_user

from typing import List

router = APIRouter(prefix="/user", tags=["user"])

# create user
@router.post('/', response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)) -> UserDisplay:
    return db_user.create_user(db, user)

# Read user
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# update user

# delete user