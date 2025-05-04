from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.pharmacy import PharmacyCreate, ShowPharmacy
from db.repository.pharmacies import (
    create_new_pharmacy,
    get_pharmacy_by_id,
    get_all_pharmacies,
    update_pharmacy,
    delete_pharmacy,
    search_medicine,
)

router = APIRouter(prefix="/pharmacies", tags=["Pharmacies"])


@router.post("/", response_model=ShowPharmacy, status_code=status.HTTP_201_CREATED)
def create_pharmacy(pharmacy: PharmacyCreate, db: Session = Depends(get_db)):
    return create_new_pharmacy(pharmacy=pharmacy, db=db)


@router.get("/{pharmacy_id}", response_model=ShowPharmacy)
def read_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    pharmacy = get_pharmacy_by_id(pharmacy_id, db)
    if not pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    return pharmacy


@router.get("/", response_model=list[ShowPharmacy], status_code=status.HTTP_200_OK)
def read_pharmacies(db: Session = Depends(get_db)):
    pharmacies = get_all_pharmacies(db)  # Fetch all pharmacies
    return pharmacies


@router.put("/{pharmacy_id}", response_model=ShowPharmacy)
def update_pharmacy_data(
    pharmacy_id: int, pharmacy: PharmacyCreate, db: Session = Depends(get_db)
):
    return update_pharmacy(pharmacy_id, pharmacy, db)


@router.delete("/{pharmacy_id}")
def remove_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    return delete_pharmacy(pharmacy_id, db)


@router.get("/search-medicine/")
def search_medicine_api(medicine_name: str, db: Session = Depends(get_db)):
    return search_medicine(medicine_name, db)
