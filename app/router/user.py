from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db.schemas import UserBase
from db import db_user

router = APIRouter(prefix="/user", tags=["user"])

# create user
@router.post('/')
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, user)

# Read user

# update user

# delete user