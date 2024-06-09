from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.users.models import User as UserModel
from core.apps.users.entities import UserEntity


class BaseUserService(ABC):
    @abstractmethod
    def get_or_create(self, phone) -> UserEntity:
        ...

    @abstractmethod
    def generate_token(self, user: UserEntity) -> str:
        ...

    def get(self, phone: str) -> UserEntity:
        ...


class ORMUserService(BaseUserService):
    def get_or_create(self, phone) -> UserEntity:
        user_dto, _ = UserModel.objects.get_or_create(phone=phone)
        return user_dto.to_entity()

    def get(self, phone: str) -> UserEntity:
        user_dto = UserModel.objects.get(phone=phone)
        return user_dto.to_entity()

    def generate_token(self, user: UserEntity) -> str:
        new_token = str(uuid4())
        UserModel.objects.filter(phone=user.phone).update(token=new_token)
        return new_token
