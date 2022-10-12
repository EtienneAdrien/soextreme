from sqlalchemy import Column, Integer, String, Interval, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.utils.database.base import Base


class CommentModel(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    score = Column(Interval, nullable=True)
    is_parent = Column(Boolean, nullable=False)

    activity_id = Column(Integer, ForeignKey("activity.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=True)

    activity = relationship("ActivityModel", back_populates="comments")
    user = relationship("UserModel", back_populates="comments")
    comment_parent = relationship("CommentModel")

