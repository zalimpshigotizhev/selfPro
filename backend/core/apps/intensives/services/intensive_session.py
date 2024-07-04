from abc import (
    ABC,
    abstractmethod,
)

from core.api.v1.intensives.schemas import IntensiveSessionAdd
from core.apps.intensives.models.intensives import Intensive as IntensiveModel
from core.apps.intensives.models.intensive_sessions import IntensiveSession


class BaseIntensiveSessionService(ABC):
    @abstractmethod
    def post_intensive_session(self, intensive_session: IntensiveSessionAdd):
        ...


class ORMIntensiveSessionService(BaseIntensiveSessionService):
    def post_intensive_session(self, id: int, intensive_session: IntensiveSessionAdd):
        intensive = IntensiveModel.objects.filter(id=id).first()
        IntensiveSession.objects.create(
            intensive=intensive,
            duration=intensive_session.duration,
        )