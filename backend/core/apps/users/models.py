from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.entities import UserEntity


class User(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Телефон пользователя',
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name='Токен пользователя',
        max_length=255,
        unique=True,
        default=uuid4(),
    )

    def to_entity(self) -> UserEntity:
        return UserEntity(phone=self.phone, created_at=self.created_at)

    def __str__(self) -> str:
        return f'{self.phone}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
