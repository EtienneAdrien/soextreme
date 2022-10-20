import datetime
from typing import Set, Optional, Union

from pydantic import BaseModel, validator, Field, PrivateAttr

from app.features.time_rule.models.time_rule import TimeRuleTypes
from app.features.time_rule.schemas.rule import RuleBase, ExistingRule


class OneOffTimeRule(BaseModel):
    date_start: datetime.date

    time_start: Optional[datetime.time]
    time_end: Optional[datetime.time]

    time_rule_type: TimeRuleTypes = Field(const=TimeRuleTypes.one_time.value, description=f"Must be equal to *{TimeRuleTypes.one_time.value}*")

    rule: Union[RuleBase, ExistingRule]


class WeeklyTimeRule(OneOffTimeRule):

    @validator("days")
    def validate_days(cls, v):
        if v:
            assert len(set(v)) <= 7

    days: Set[int]

    time_rule_type: TimeRuleTypes = Field(const=TimeRuleTypes.weekly.value, description=f"Must be equal to *{TimeRuleTypes.weekly.value}*")


class MonthlyTimeRule(OneOffTimeRule):
    class Config:
        time_rule_type = TimeRuleTypes.monthly.value

    date_end: Optional[datetime.date]

    time_rule_type: TimeRuleTypes = Field(const=TimeRuleTypes.monthly.value, description=f"Must be equal to *{TimeRuleTypes.monthly.value}*")


class YearlyTimeRule(OneOffTimeRule):
    class Config:
        time_rule_type = TimeRuleTypes.yearly.value

    date_end: Optional[datetime.date]

    time_rule_type: TimeRuleTypes = Field(const=TimeRuleTypes.yearly.value, description=f"Must be equal to *{TimeRuleTypes.yearly.value}*")


def get_schema(time_rule_type: TimeRuleTypes):
    pass