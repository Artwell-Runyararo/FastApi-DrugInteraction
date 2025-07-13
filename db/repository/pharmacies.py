from sqlalchemy.orm import Session
from schemas.pharmacy import PharmacyCreate
from db.models.pharmacies import Pharmacy
from db.models.pharmacystocks import PharmacyStock
from db.models.stock import Medicine


def create_new_pharmacy(pharmacy: PharmacyCreate, db: Session):
    new_pharmacy = Pharmacy(
        name=pharmacy.name,
        email=pharmacy.email,
        address=pharmacy.address,
        phone=pharmacy.phone,
    )
    db.add(new_pharmacy)
    db.commit()
    db.refresh(new_pharmacy)
    return new_pharmacy


def get_pharmacy_by_id(pharmacy_id: int, db: Session):
    return db.query(Pharmacy).filter(Pharmacy.pharmacy_id == pharmacy_id).first()


def get_all_pharmacies(db: Session):
    return db.query(Pharmacy).all()


def update_pharmacy(pharmacy_id: int, pharmacy: PharmacyCreate, db: Session):
    db_pharmacy = db.query(Pharmacy).filter(Pharmacy.pharmacy_id == pharmacy_id).first()
    if db_pharmacy:
        for key, value in pharmacy.dict().items():
            setattr(db_pharmacy, key, value)
        db.commit()
        db.refresh(db_pharmacy)
    return db_pharmacy


def delete_pharmacy(pharmacy_id: int, db: Session):
    db_pharmacy = db.query(Pharmacy).filter(Pharmacy.pharmacy_id == pharmacy_id).first()
    if db_pharmacy:
        db.delete(db_pharmacy)
        db.commit()
    return {"message": "Pharmacy deleted successfully"}


def search_medicine(medicine_name: str, db: Session):
    results = (
        db.query(PharmacyStock)
        .join(Pharmacy, PharmacyStock.pharmacy_id == Pharmacy.pharmacy_id)
        .join(Medicine, PharmacyStock.medic_id == Medicine.medic_id)  # Join Medicine
        .filter(Medicine.name.ilike(f"%{medicine_name}%"))  # Search by medicine name
        .all()
    )

    return [
        {
            "pharmacy_name": result.pharmacy.name,
            "address": result.pharmacy.address,
            "medicine": result.medicine.name,  # Use medicine name from Medicine model
            "stock": result.quantity_in_stock,  # Use correct field name for stock
            "price": result.price,  # Include price if needed
            # 👇 Add location info (use first location if multiple exist)
            "latitude": (
                result.pharmacy.locations[0].latitude
                if result.pharmacy.locations
                else None
            ),
            "longitude": (
                result.pharmacy.locations[0].longitude
                if result.pharmacy.locations
                else None
            ),
        }
        for result in results
    ]
