from dataclasses import dataclass, field
from datetime import datetime

from .model import Model
from ..utillities.constants import Constants


@dataclass
class Staff(Model):
    visitor_id: int
    name: str
    work_type: Constants.WorkType
    entry_timestamp: datetime
    national_id: str
    exit_timestamp: datetime
