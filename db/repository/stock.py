from sqlalchemy.orm import Session
from schemas.stock import MedicineCreate
from db.models.stock import Medicine


def create_new_medicine(
    medicine: MedicineCreate,
    db: Session,
    pharmacy_id: int,
):
    new_medicine = Medicine(
        name=medicine.name,
        dosage=medicine.dosage,
        pharmacy_id=pharmacy_id,
    )
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return new_medicine


def get_medicine_by_id(medic_id: int, db: Session, pharmacy_id: int):
    return (
        db.query(Medicine)
        .filter(Medicine.medic_id == medic_id, Medicine.pharmacy_id == pharmacy_id)
        .first()
    )


def get_all_medicines(
    db: Session,
    pharmacy_id: int,
):
    return db.query(Medicine).filter(Medicine.pharmacy_id == pharmacy_id).all()


def update_medicine(
    medicine_id: int, medicine: MedicineCreate, db: Session, pharmacy_id: int
):
    db_medicine = (
        db.query(Medicine)
        .filter(Medicine.medic_id == medicine_id, Medicine.pharmacy_id == pharmacy_id)
        .first()
    )
    if db_medicine:
        for key, value in medicine.dict().items():
            setattr(db_medicine, key, value)
        db.commit()
        db.refresh(db_medicine)
    return db_medicine


def delete_medicine(medicine_id: int, db: Session, pharmacy_id: int):
    db_medicine = (
        db.query(Medicine)
        .filter(
            Medicine.medic_id == medicine_id,
            Medicine.pharmacy_id == pharmacy_id,
        )
        .first()
    )
    if db_medicine:
        db.delete(db_medicine)
        db.commit()
    return {"message": "Medicine deleted successfully"}
