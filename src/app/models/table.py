from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from src.app.models.base import Base


class Table(Base):
    __tablename__ = 'tables'

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    seats: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String(50), nullable=False)


    def __repr__(self) -> str:
        return (f'| '
                f'id: {self.id}, '
                f'seats: {self.seats}, '
                f'location: {self.location}'
                f' |')
