from sqlalchemy.orm import Session
from schemas.location import LocationCreate
from db.models.locations import Location


def create_new_location(location: LocationCreate, db: Session):
    new_location = Location(
        pharmacy_id=location.pharmacy_id,
        latitude=location.latitude,
        longitude=location.longitude,
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location


def get_location_by_id(location_id: int, db: Session):
    return db.query(Location).filter(Location.location_id == location_id).first()


def get_all_locations(db: Session):
    return db.query(Location).all()


def update_location(location_id: int, location: LocationCreate, db: Session):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        for key, value in location.dict().items():
            setattr(db_location, key, value)
        db.commit()
        db.refresh(db_location)
    return db_location


def delete_location(location_id: int, db: Session):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
    return {"message": "Location deleted successfully"}
