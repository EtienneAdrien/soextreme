from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.features.activity import crud
from app.features.activity.schemas.activity import ActivityCreate
from app.utils.database.connection import get_db

activity_router = APIRouter(
    prefix="/activity"
)

@activity_router.post("/")
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(activity=activity, db=db)