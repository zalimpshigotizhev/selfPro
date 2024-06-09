from ninja import Router
from django.http import HttpRequest
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.users.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.users.services.auth import AuthService
from core.apps.users.services.codes import DjangoCacheCodeService
from core.apps.users.services.users import ORMUserService
from core.apps.users.services.senders import DummySenderService


router = Router(tags=['USER'])


@router.post('auth', response=ApiResponse[AuthOutSchema], operation_id='authorize')
def auth_handler(request: HttpRequest, schema: AuthInSchema) -> ApiResponse[AuthOutSchema]:
    service = AuthService(
        user_service=ORMUserService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )
    service.authorize(schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f'Код отправлен на номер {schema.phone}',
        ),
    )


@router.post('confirm', response=ApiResponse[TokenOutSchema], operation_id='confirm-code')
def get_token_handler(request: HttpRequest, schema: TokenInSchema) -> ApiResponse[TokenOutSchema]:
    service = AuthService(
        user_service=ORMUserService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )

    try:
        token = service.confirm(code=schema.code, phone=schema.phone)

    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message='Неверный код',
        ) from exception

    return ApiResponse(
        data=TokenOutSchema(
            token=token,
        ),
    )
