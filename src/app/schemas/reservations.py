from datetime import datetime, timedelta, tzinfo, timezone

from pydantic import BaseModel, Field
from pydantic.v1 import validator


class ReservationCreateScheme(BaseModel):
    customer_name: str = Field(max_length=50)
    table_id: int = Field(gt=0)
    duration_minutes: int = Field(gt=0)
    reservation_time: datetime



class ReservationDeleteScheme(BaseModel):
    id: int = Field(gt=0)


class ReservationScheme(ReservationCreateScheme, ReservationDeleteScheme):
    pass

