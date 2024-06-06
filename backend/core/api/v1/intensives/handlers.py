from ninja import (
    Query,
    Router,
)
from django.http import HttpRequest

from core.api.filters import PaginationIn
from core.api.schemas import (
    ApiResponse,
    PaginationOut,
    ListPaginatedResponse,
)
from core.api.v1.intensives.filters import IntensiveFilters
from core.api.v1.intensives.schemas import IntensiveSchema
from core.apps.intensives.services.intensive import (
    ORMIntensiveService,
    BaseIntensiveService,
)


router = Router(tags=['INTENSIVE'])


@router.get('', response=ApiResponse[ListPaginatedResponse[IntensiveSchema]])
def intensive_list(
    request: HttpRequest,
    filters: Query[IntensiveFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[IntensiveSchema]]:
    service: BaseIntensiveService = ORMIntensiveService()
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
