from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.base_class import Base


class PharmacyStock(Base):
    __tablename__ = "pharmacy_stock"

    stock_id = Column(Integer, primary_key=True, index=True)
    pharmacy_id = Column(Integer, ForeignKey("pharmacies.pharmacy_id"))
    medic_id = Column(Integer, ForeignKey("medicines.medic_id"))
    quantity_in_stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    pharmacy = relationship("Pharmacy", back_populates="stocks")
    medicine = relationship("Medicine", back_populates="stocks")
