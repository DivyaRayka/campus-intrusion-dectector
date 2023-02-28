from dataclasses import dataclass
from staff import Staff
from datetime import datetime
from .model import  Model


@dataclass
class Visitor(Model):
    visitor_id: int
    name: str
    staff_ids: list[Staff]
    entry_timestamp: datetime
    national_id: str
    exit_timestamp: datetime
