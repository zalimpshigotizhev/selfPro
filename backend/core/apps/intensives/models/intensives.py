from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.intensives.entities.intensives import Intensive as IntensiveEntity
from core.constants import limits


class Intensive(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название интенсива",
        
        max_length=limits.ML_TITLE_INTENSIVE,
    )
    color = models.CharField(
        verbose_name="Цвет интенсива",
        max_length=limits.ML_COLOR_INTENSIVE,
    )
    
    def to_entity(self) -> IntensiveEntity:
        return IntensiveEntity(
            id=self.id,
            title=self.title,
            color=self.color,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Интенсив"
        verbose_name_plural = "Интенсивы"
        
    