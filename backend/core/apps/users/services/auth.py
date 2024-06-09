from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.users.services.codes import BaseCodeService
from core.apps.users.services.users import BaseUserService
from core.apps.users.services.senders import BaseSenderService


@dataclass
class BaseAuthService(ABC):
    user_service: BaseUserService
    codes_service: BaseCodeService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, phone: str):
        ...

    @abstractmethod
    def confirm(self, code: str, phone: str):
        ...


class AuthService(BaseAuthService):
    def authorize(self, phone: str):
        user = self.user_service.get_or_create(phone=phone)
        code = self.codes_service.generate_code(user=user)
        self.sender_service.send_code(user=user, code=code)

    def confirm(self, code: str, phone: str):
        user = self.user_service.get(phone=phone)
        self.codes_service.validate_code(code=code, user=user)
        return self.user_service.generate_token(user)
