from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, DateTime

from src.app.models.base import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    customer_name: Mapped[str] = mapped_column(String(50), nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey('tables.id'))
    reservation_time: Mapped[DateTime] = mapped_column(DateTime)
    duration_minutes: Mapped[int]


    def __repr__(self) -> str:
        return (f'| '
                f'id: {self.id}, '
                f'customer_name: {self.customer_name}, '
                f'table_id: {self.table_id}, '
                f'reservation_time: {self.reservation_time}, '
                f'duration_minutes: {self.duration_minutes}'
                f' |')
