from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.users import User
from db.models.patients import Patient
from core.security import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()


# Patient Login
@router.post("/login/patient")
def login_patient(email: str, password: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.email == email).first()
    if not patient or not verify_password(password, patient.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": patient.email, "role": "patient"})
    return {"access_token": token, "token_type": "bearer"}


# User (Pharmacy Staff) Login
@router.post("/login/user")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Ensure the user is assigned to a pharmacy
    if not user.pharmacy_id:
        raise HTTPException(
            status_code=403, detail="User is not assigned to a pharmacy"
        )

    token = create_access_token(
        {"sub": user.email, "role": "user", "pharmacy_id": user.pharmacy_id}
    )
    return {"access_token": token, "token_type": "bearer"}
