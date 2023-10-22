from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db.schemas import UserBase, UserDisplay
from db import db_user

router = APIRouter(prefix="/user", tags=["user"])

# create user
@router.post('/', response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)) -> UserDisplay:
    return db_user.create_user(db, user)

# Read user

# update user

# delete user