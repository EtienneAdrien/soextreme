from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class RuleModel(Base):
    __tablename__ = "rule"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    rule_type = Column(String, nullable=False)
    parameters = Column(JSON, nullable=False)
    is_global = Column(Boolean, default=False)

    company_id = Column(Integer, ForeignKey("company.id"), nullable=True)
    company = relationship("CompanyModel", back_populates="rules")

    time_rules = relationship("TimeRuleModel", back_populates="rule")




