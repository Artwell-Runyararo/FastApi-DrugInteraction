from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Medicine(Base):
    __tablename__ = "medicines"

    medic_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    pharmacy_id = Column(Integer, ForeignKey("pharmacies.pharmacy_id"))

    # Relationship
    stocks = relationship("PharmacyStock", back_populates="medicine")
