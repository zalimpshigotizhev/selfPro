from abc import abstractmethod

from core.apps.users.entities import UserEntity


class BaseSenderService:
    @abstractmethod
    def send_code(self, user: UserEntity, code: str) -> None:
        ...


class DummySenderService(BaseSenderService):
    def send_code(self, user: UserEntity, code: str) -> None:
        print(f"Send code: {code} to {user}")
