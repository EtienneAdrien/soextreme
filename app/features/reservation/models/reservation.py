from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class ReservationModel(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    paid = Column(Boolean, default=False)
    is_gift = Column(Boolean, default=False)
    cancelled = Column(Boolean, default=False)
    created_at = Column(DateTime)
    quantity = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    activity_id = Column(Integer, ForeignKey("activity.id"))
    time_rule_id = Column(Integer, ForeignKey("time_rule.id"))

    user = relationship("UserModel", back_populates="reservations")
    activity = relationship("ActivityModel", back_populates="reservations")
    time_rule = relationship("TimeRuleModel", back_populates="reservation")
