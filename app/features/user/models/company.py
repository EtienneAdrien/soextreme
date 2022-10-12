from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class CompanyModel(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    users = relationship("UserModel", back_populates="company")
    rules = relationship("RuleModel", back_populates="company")