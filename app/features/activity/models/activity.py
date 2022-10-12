from sqlalchemy import Column, Integer, String, Boolean

from app.utils.database.base import Base


class ActivityModel(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    desc = Column(String)
    is_active = Column(Boolean, default=True)
