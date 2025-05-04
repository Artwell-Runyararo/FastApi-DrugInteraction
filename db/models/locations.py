from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    pharmacy_id = Column(Integer, ForeignKey("pharmacies.pharmacy_id"))
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    pharmacy = relationship("Pharmacy", back_populates="locations")
