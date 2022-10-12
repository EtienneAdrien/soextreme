from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.features.activity.models.activity_tag import activity_tag
from app.utils.database.base import Base


class TagModel(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False, unique=True)
    is_category = Column(Boolean, nullable=False, default=False)

    activities_for_category = relationship("ActivityModel", back_populates="category")
    activities_for_tag = relationship("ActivityModel", secondary=activity_tag)
