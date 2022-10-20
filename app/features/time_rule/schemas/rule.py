from typing import Dict, Any

from pydantic import BaseModel


class RuleBase(BaseModel):
    label: str
    rule_type: str
    parameters: Dict[str, Any]
    is_global: bool


class ExistingRule(BaseModel):
    id: int
