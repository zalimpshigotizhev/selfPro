from ninja import (
    Query,
    Router,
)
from django.http import HttpRequest
from ninja.security import django_auth

from core.api.filters import PaginationIn
from core.api.schemas import (
    ApiResponse,
    PaginationOut,
    ListPaginatedResponse,
)
from core.api.v1.intensives.filters import IntensiveFilters
from core.api.v1.intensives.schemas import (
    IntensiveCreate,
    IntensiveSchema,
    IntensiveSessionAdd,
)
from core.apps.intensives.containers import get_container
from core.apps.intensives.services.intensive import BaseIntensiveService
from core.apps.intensives.services.intensive_session import BaseIntensiveSessionService


router = Router(tags=['INTENSIVE'])


@router.get('', response=ApiResponse[ListPaginatedResponse[IntensiveSchema]])
def intensive_list(
    request: HttpRequest,
    filters: Query[IntensiveFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[IntensiveSchema]]:
    container = get_container()
    
    service = container.resolve(BaseIntensiveService)
    intensive_list = service.get_intensive_list(
        filters=filters,
        pagination=pagination_in,
    )

    intensive_count = service.get_intensive_count(filters=filters)
    items = [IntensiveSchema.from_entity(obj) for obj in intensive_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=intensive_count,
    )

    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out),
    )


@router.post('')
def intensive_create(
    request: HttpRequest,
    new_intensive: Query[IntensiveCreate],
):
    container = get_container()

    service = container.resolve(BaseIntensiveService)

    service.post_intensive_create(new_intensive)

    return ApiResponse(data="ok") 


@router.post('/{id}')
def add_intensive_session(
    request: HttpRequest,
    id,
    new_intensive: Query[IntensiveSessionAdd],
):
    container = get_container()
    service = container.resolve(BaseIntensiveSessionService)

    service.post_intensive_session(id, new_intensive)
    return ApiResponse(data="ok")


@router.get("/bearer", auth=django_auth)
def bearer(request):
    return {"token": request.auth}