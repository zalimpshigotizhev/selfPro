from abc import ABC, abstractmethod
from typing import Iterable

from core.api.v1.intensives.schemas import IntensiveSchema
from core.apps.intensives.entities.intensives import Intensive
from core.apps.intensives.models.intensives import Intensive as IntensiveModel

class BaseIntensiveService(ABC):
    @abstractmethod
    def get_intensive_list(self) -> Iterable[Intensive]:
        ...
    @abstractmethod
    def get_intensive_count(self) -> Iterable[Intensive]:
        ...
      
class ORMIntensiveService(BaseIntensiveService):
    def get_intensive_list(self) -> Iterable[Intensive]:
        qs = IntensiveModel.objects.filter()
        
        return [intensive.to_entity() for intensive in qs]
    
    def get_intensive_count(self) -> Iterable[Intensive]:
        return IntensiveModel.objects.filter().count()