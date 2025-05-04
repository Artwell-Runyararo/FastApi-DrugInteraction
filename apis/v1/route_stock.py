from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.stock import MedicineCreate, ShowMedicine
from db.session import get_db
from core.security import get_current_user

from db.repository.stock import (
    create_new_medicine,
    get_medicine_by_id,
    get_all_medicines,
    update_medicine,
    delete_medicine,
)

router = APIRouter()


@router.post("/", response_model=ShowMedicine, status_code=status.HTTP_201_CREATED)
def create_medicine(
    medicine: MedicineCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return create_new_medicine(medicine=medicine, pharmacy_id=pharmacy_id, db=db)


@router.get("/{medicine_id}", response_model=ShowMedicine)
def read_medicine(
    medicine_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    medicine = get_medicine_by_id(medicine_id, db, pharmacy_id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine


@router.get("/", response_model=list[ShowMedicine])
def read_medicines(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return get_all_medicines(db, pharmacy_id)


@router.put("/{medicine_id}", response_model=ShowMedicine)
def update_medicine_data(
    medicine_id: int,
    medicine: MedicineCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return update_medicine(medicine_id, medicine, db, pharmacy_id)


@router.delete("/{medicine_id}")
def remove_medicine(
    medicine_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return delete_medicine(medicine_id, db, pharmacy_id)
