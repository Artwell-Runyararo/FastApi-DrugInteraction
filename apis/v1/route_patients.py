from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.patients import PatientCreate, ShowPatient
from db.session import get_db
from db.repository.patients import (
    create_new_patient,
    get_patient_by_email,
    get_patient_by_id,
    get_all_patients,
    update_patient,
    delete_patient,
)

router = APIRouter()


@router.post("/", response_model=ShowPatient, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    existing_patient = get_patient_by_email(patient.email, db)
    if existing_patient:
        raise HTTPException(status_code=400, detail="Email already registered")
    patient = create_new_patient(patient=patient, db=db)
    return patient


@router.get("/{patient_id}", response_model=ShowPatient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient_by_id(patient_id, db)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.get("/", response_model=list[ShowPatient])
def read_patients(db: Session = Depends(get_db)):
    return get_all_patients(db)


@router.put("/{patient_id}", response_model=ShowPatient)
def update_patient_data(
    patient_id: int, patient: PatientCreate, db: Session = Depends(get_db)
):
    return update_patient(patient_id, patient, db)


@router.delete("/{patient_id}")
def remove_patient(patient_id: int, db: Session = Depends(get_db)):
    return delete_patient(patient_id, db)
