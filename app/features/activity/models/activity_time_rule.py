from sqlalchemy import Table, Column, ForeignKey

from app.utils.database.base import Base

activity_time_rule = Table(
    "activity_time_rule",
    Base.metadata,
    Column("time_rule_id", ForeignKey("time_rule.id"), primary_key=True),
    Column("activity_id", ForeignKey("activity.id"), primary_key=True),
)
