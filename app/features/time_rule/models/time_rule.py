import enum

from sqlalchemy import Column, Integer, Time, Enum, ForeignKey, Date
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class TimeRuleTypes(enum.Enum):
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"
    one_time = "one_time"


class TimeRuleModel(Base):
    """
    Weekly:
        - days = [1, 2, 3, 4, 5]
        - time_start = 09:00
        - time_end = 12:00
        - date_start = 01-01-2022
    Monthly:
        - date_start = 01-01-2022
        - date_end = 02-01-2022
        - time_start = 09:00
        - time_end = 12:00
    One-time:
        - date_start = 01-01-2022
        - time_start = 09:00
        - time_end = 12:00
    """
    __tablename__ = "time_rule"

    id = Column(Integer, primary_key=True, index=True)
    date_start = Column(Date)
    date_end = Column(Date, nullable=True)
    time_start = Column(Time, nullable=True)
    time_end = Column(Time, nullable=True)
    days = Column(ARRAY(Integer, dimensions=2), nullable=True)

    time_rule_type = Column(Enum(TimeRuleTypes))

    rule_id = Column(Integer, ForeignKey("rule.id"))

    rule = relationship("RuleModel", back_populates="time_rules")
    reservation = relationship("ReservationModel", back_populates="time_rule")


