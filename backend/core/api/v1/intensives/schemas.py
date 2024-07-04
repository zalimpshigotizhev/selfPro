from typing import Any
from datetime import datetime

from pydantic import (
    BaseModel,
    Base64UrlStr,
)

from core.apps.intensives.entities.intensives import Intensive as IntensiveEntity


class IntensiveSchema(BaseModel):
    id: int # noqa
    title: str
    color: str
    created_at: datetime
    updated_at: datetime | None
    image_url: str | None

    @staticmethod
    def from_entity(entity: IntensiveEntity) -> 'IntensiveSchema':
        return IntensiveSchema(
            id=entity.id,
            title=entity.title,
            color=entity.color,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            image_url=entity.image_url,
        )


class IntensiveCreate(BaseModel):
    title: str
    color: str


class IntensiveSessionAdd(BaseModel):
    duration: int
