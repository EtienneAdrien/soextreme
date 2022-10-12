from sqlalchemy import Table, Column, ForeignKey

from app.utils.database.base import Base

activity_tag = Table(
    "activity_tag",
    Base.metadata,
    Column("activity_id", ForeignKey("activity.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)
