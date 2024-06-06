from ninja import Schema


class IntensiveFilters(Schema):
    search: str | None = None
