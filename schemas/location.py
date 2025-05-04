from pydantic import BaseModel, EmailStr


class LocationCreate(BaseModel):
    pharmacy_id: int
    latitude: str
    longitude: str


class LocationUpdate(LocationCreate):
    pass


class ShowLocation(LocationCreate):
    location_id: int

    class Config:
        from_attributes = True
