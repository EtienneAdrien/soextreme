from typing import List, Union

from pydantic import BaseModel

from app.features.time_rule.schemas.time_rule import OneOffTimeRule, WeeklyTimeRule, MonthlyTimeRule, YearlyTimeRule


class ActivityBase(BaseModel):
    description: str
    title: str
    duration: str
    price: int
    capacity: int


class ActivityCreate(ActivityBase):
    time_rules: List[Union[OneOffTimeRule, WeeklyTimeRule, MonthlyTimeRule, YearlyTimeRule]]


class Activity(ActivityBase):
    id: int

    class Config:
        orm_mode = True
