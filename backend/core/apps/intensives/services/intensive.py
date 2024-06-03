from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.intensives.filters import IntensiveFilters
from core.apps.intensives.entities.intensives import Intensive
from core.apps.intensives.models.intensives import Intensive as IntensiveModel

class BaseIntensiveService(ABC):
    @abstractmethod
    def get_intensive_list(self, filters: IntensiveFilters, pagination: PaginationIn) -> Iterable[Intensive]:
        ...
    @abstractmethod
    def get_intensive_count(self, filters: IntensiveFilters) -> Iterable[Intensive]:
        ...
   
# TODO: Закинуть фильтры в сервисный слой, чтобы избежать D из SOLID
class ORMIntensiveService(BaseIntensiveService):
    def _build_intensive_query(self, filters: IntensiveFilters) -> Q:
        query = Q()

        if filters.search is not None:
            query &= Q(title__icontains=filters.search)

        return query
    
    def get_intensive_list(self, filters: IntensiveFilters, pagination: PaginationIn) -> Iterable[Intensive]:
        query = self._build_intensive_query(filters)
        qs = IntensiveModel.objects.filter(query)[pagination.offset:pagination.offset + pagination.limit]
        
        return [intensive.to_entity() for intensive in qs]
    
    def get_intensive_count(self, filters: IntensiveFilters) -> Iterable[Intensive]:
        query = self._build_intensive_query(filters)
        return IntensiveModel.objects.filter(query).count()