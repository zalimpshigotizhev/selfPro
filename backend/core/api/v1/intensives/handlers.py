from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListPaginatedResponse, PaginationOut
from core.api.v1.intensives.schemas import IntensiveSchema
from core.apps.intensives.services.intensive import BaseIntensiveService, ORMIntensiveService


router = Router(tags=['INTENSIVE'], )


@router.get('', response=ApiResponse[ListPaginatedResponse[IntensiveSchema]])
def intensive_list(request: HttpRequest) -> ApiResponse[ListPaginatedResponse[IntensiveSchema]]:
    service: BaseIntensiveService = ORMIntensiveService()
    intensive_list = service.get_intensive_list() 
    
    intensive_count = service.get_intensive_count()
    items =  [IntensiveSchema.from_entity(obj) for obj in intensive_list]
    pagination = PaginationOut(
        offset=0,
        limit=intensive_count,
        total=intensive_count
    )
    
    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination))