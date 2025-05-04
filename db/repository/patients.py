from sqlalchemy.orm import Session
from schemas.patients import PatientCreate
from db.models.patients import Patient
from core.hashing import Hasher


def create_new_patient(patient: PatientCreate, db: Session):
    new_patient = Patient(
        name=patient.name,
        email=patient.email,
        password=Hasher.get_password_hash(patient.password),
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def get_patient_by_email(email: str, db: Session):
    return db.query(Patient).filter(Patient.email == email).first()


def get_patient_by_id(patient_id: int, db: Session):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()


def get_all_patients(db: Session):
    return db.query(Patient).all()


def update_patient(patient_id: int, patient: PatientCreate, db: Session):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient


def delete_patient(patient_id: int, db: Session):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return {"message": "Patient deleted successfully"}
