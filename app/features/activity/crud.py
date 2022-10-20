from sqlalchemy.orm import Session

from app.features import models
from app.features.activity.schemas.activity import ActivityCreate


def create_activity(activity: ActivityCreate, db: Session):
    db_item = models.ActivityModel(**activity.dict())
    db.add(db_item)
    db.commit()
