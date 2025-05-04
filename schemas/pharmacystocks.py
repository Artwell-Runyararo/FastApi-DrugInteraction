from pydantic import BaseModel
from schemas.pharmacy import ShowPharmacy
from schemas.stock import ShowMedicine


class PharmacyStockBase(BaseModel):
    medic_id: int
    quantity_in_stock: int
    price: float


class PharmacyStockCreate(PharmacyStockBase):
    pass


class PharmacyStockShow(PharmacyStockBase):
    stock_id: int
    pharmacy: ShowPharmacy
    medicine: ShowMedicine

    class Config:
        from_attributes = True
