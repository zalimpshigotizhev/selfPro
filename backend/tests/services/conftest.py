import pytest

from core.apps.intensives.services.intensive import (
    ORMIntensiveService,
    BaseIntensiveService,
)


@pytest.fixture
def intensive_service() -> BaseIntensiveService:
    return ORMIntensiveService()
