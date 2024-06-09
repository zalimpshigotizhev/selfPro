from datetime import datetime
from dataclasses import dataclass


@dataclass
class UserEntity:
    phone: str
    created_at: datetime
