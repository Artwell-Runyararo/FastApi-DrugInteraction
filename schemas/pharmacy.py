from pydantic import BaseModel, EmailStr


class PharmacyCreate(BaseModel):
    name: str
    email: EmailStr
    address: str
    phone: str


class UpdatePharmacy(PharmacyCreate):
    pass


class ShowPharmacy(BaseModel):
    pharmacy_id: int  # ✅ Correct
    name: str
    email: EmailStr
    address: str
    phone: str

    class Config:
        from_attributes = True
