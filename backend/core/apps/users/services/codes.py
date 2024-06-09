import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.users.entities import UserEntity
from core.apps.users.exceptions.codes import (
    CodeNotEqualException,
    CodeNotFoundException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, user: UserEntity):
        ...

    @abstractmethod
    def validate_code(self, code: str, user: UserEntity) -> None:
        ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, user: UserEntity) -> str:
        code = str(random.SystemRandom.randint(100000, 999999))
        cache.set(user.phone, code)
        return code

    def validate_code(self, code: str, user: UserEntity) -> None:
        cached_code = cache.get(user.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodeNotEqualException(
                code=code,
                cached_code=cached_code,
                user_phone=user.phone,
            )

        cache.delete(user.phone)
