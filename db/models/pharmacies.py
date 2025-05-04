from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.base_class import Base


class Pharmacy(Base):
    __tablename__ = "pharmacies"

    pharmacy_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    users = relationship("User", back_populates="pharmacy")
    stocks = relationship("PharmacyStock", back_populates="pharmacy")
    locations = relationship("Location", back_populates="pharmacy")
