from ninja import Schema

from core.api.filters import DefaultFilter

class IntensiveFilters(Schema):
    search: str | None