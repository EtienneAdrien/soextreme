import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class AddressModel(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    region = Column(String, nullable=False)

    user = relationship("UserModel", back_populates="address", uselist=False)
    activity = relationship("ActivityModel", back_populates="address", uselist=False)
