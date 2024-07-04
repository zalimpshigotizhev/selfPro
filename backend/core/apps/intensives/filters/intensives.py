from dataclasses import dataclass


@dataclass
class IntensiveFiltersEnity(BaseModel):
    search: str | None = None
