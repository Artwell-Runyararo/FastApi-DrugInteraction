from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    new_user = User(
        name=user.name,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        pharmacy_id=user.pharmacy_id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.user_id == user_id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def update_user(user_id: int, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return {"message": "User deleted successfully"}
