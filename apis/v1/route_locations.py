from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.location import LocationCreate, ShowLocation
from db.session import get_db
from db.repository.locations import (
    create_new_location,
    get_location_by_id,
    get_all_locations,
    update_location,
    delete_location,
)

router = APIRouter()


@router.post("/", response_model=ShowLocation, status_code=status.HTTP_201_CREATED)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    return create_new_location(location, db)


@router.get("/{location_id}", response_model=ShowLocation)
def read_location(location_id: int, db: Session = Depends(get_db)):
    location = get_location_by_id(location_id, db)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.get("/", response_model=list[ShowLocation])
def read_locations(db: Session = Depends(get_db)):
    return get_all_locations(db)


@router.put("/{location_id}", response_model=ShowLocation)
def update_location_data(
    location_id: int, location: LocationCreate, db: Session = Depends(get_db)
):
    return update_location(location_id, location, db)


@router.delete("/{location_id}")
def remove_location(location_id: int, db: Session = Depends(get_db)):
    return delete_location(location_id, db)
