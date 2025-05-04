from pydantic import BaseModel, EmailStr


class MedicineCreate(BaseModel):
    name: str
    dosage: str


class MedicineUpdate(MedicineCreate):
    pass


class ShowMedicine(MedicineCreate):
    medic_id: int
    name: str
    dosage: str

    class Config:
        from_attributes = True
