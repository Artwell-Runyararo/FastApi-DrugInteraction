from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import (
    create_new_user,
    get_user_by_email,
    get_user_by_id,
    get_all_users,
    update_user,
    delete_user,
)

router = APIRouter()


@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(user.email, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_new_user(user=user, db=db)
    return ShowUser.model_validate(user)


@router.get("/{user_id}", response_model=ShowUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[ShowUser])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.put("/{user_id}", response_model=ShowUser)
def update_user_data(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(user_id, user, db)


@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)
