import pytest
from tests.factories.intensives import IntensiveModelFactory

from core.api.filters import PaginationIn
from core.api.v1.intensives.filters import IntensiveFilters
from core.apps.intensives.services.intensive import BaseIntensiveService


@pytest.mark.django_db
def test_get_intensives_count_zero(intensive_service: BaseIntensiveService) -> None:
    """Test product count zero with no intensives in the database."""
    intensive_count = intensive_service.get_intensive_count(IntensiveFilters())
    assert intensive_count == 0, f"{intensive_count=}"


@pytest.mark.django_db
def test_get_intensives_count_exist(intensive_service: BaseIntensiveService) -> None:
    """Test product count exist with no intensives in the database."""
    expected_intensive_count = 12
    IntensiveModelFactory.create_batch(size=expected_intensive_count)

    intensive_count = intensive_service.get_intensive_count(IntensiveFilters())
    assert intensive_count == expected_intensive_count, f"{intensive_count} != "


@pytest.mark.django_db
def test_get_intensives_all(intensive_service: BaseIntensiveService):
    expected_intensive_count = 5
    intensives = IntensiveModelFactory.create_batch(size=expected_intensive_count)
    intensive_titles = {intensive.title for intensive in intensives}

    fetched_intensives = intensive_service.get_intensive_list(IntensiveFilters(), PaginationIn())
    fetched_titles = {fetched_intensive.title for fetched_intensive in fetched_intensives}

    assert len(fetched_titles) == expected_intensive_count, f'{fetched_titles=}'
    assert intensive_titles == fetched_titles, f'{intensive_titles=}'
