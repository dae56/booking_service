from pydantic import BaseModel, Field


class TableCreateScheme(BaseModel):
    name: str = Field(max_length=50)
    seats: int = Field(gt=0, lt=150)
    location: str = Field(max_length=50)


class TableDeleteScheme(BaseModel):
    id: int = Field(gt=0)


class TableScheme(TableCreateScheme, TableDeleteScheme):
    pass
