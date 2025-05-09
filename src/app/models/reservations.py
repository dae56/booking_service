from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime

from src.app.models.base import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    customer_name: Mapped[str] = mapped_column(String(50), nullable=False)
    table_id: Mapped[int | None] = mapped_column(ForeignKey('tables.id'))
    reservation_time: Mapped[datetime]
    duration_minutes: Mapped[int]
    table = relationship('Table', back_populates='reservations', uselist=False)


    def __repr__(self) -> str:
        return (f'| '
                f'id: {self.id}, '
                f'customer_name: {self.customer_name}, '
                f'table_id: {self.table_id}, '
                f'reservation_time: {self.reservation_time}, '
                f'duration_minutes: {self.duration_minutes}'
                f' |')
