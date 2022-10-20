from sqlalchemy import Column, Integer, String, Interval, ForeignKey
from sqlalchemy.orm import relationship

from app.features.activity.models.activity_tag import activity_tag
from app.features.activity.models.activity_time_rule import activity_time_rule
from app.utils.database.base import Base


class ActivityModel(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    duration = Column(Interval, nullable=False)
    price = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey("tag.id"))
    address_id = Column(Integer, ForeignKey("address.id"))

    category = relationship("TagModel", back_populates="activities_for_category")
    address = relationship("AddressModel", back_populates="activity")
    reservations = relationship("ReservationModel", back_populates="activity")
    comments = relationship("CommentModel", back_populates="activity")

    tags = relationship("TagModel", secondary=activity_tag)
    time_rules = relationship("TimeRuleModel", secondary=activity_time_rule)



