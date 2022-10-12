import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class Roles(enum.Enum):
    basic = "basic"
    manager = "manager"
    admin = "admin"


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    role = Column(Enum(Roles), nullable=False)
    created_at = Column(DateTime, nullable=False)
    last_connection = Column(DateTime)

    address_id = Column(Integer, ForeignKey("address.id"))
    company_id = Column(Integer, ForeignKey("company.id"))

    address = relationship("AddressModel", back_populates="user")
    company = relationship("CompanyModel", back_populates="users")
    reservations = relationship("ReservationModel", back_populates="user")
    comments = relationship("CommentModel", back_populates="user")
