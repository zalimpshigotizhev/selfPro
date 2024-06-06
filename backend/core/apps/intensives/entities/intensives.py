from datetime import datetime
from dataclasses import dataclass


@dataclass
class Intensive:
    id: int # noqa
    title: str
    color: str
    created_at: datetime
    updated_at: datetime
