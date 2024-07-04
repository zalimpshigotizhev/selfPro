from django.db import models

from core.apps.common.models import TimedBaseModel


class IntensiveSession(TimedBaseModel):
    intensive = models.ForeignKey(to="Intensive", on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.intensive.title + " - " + str(self.duration)
    
    class Meta:
        verbose_name = "Сессия интенсива"
        verbose_name_plural = "Сессии интенсивов"