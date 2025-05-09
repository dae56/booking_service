import asyncio
from datetime import datetime
from shutil import which

from sqlalchemy import select, table, delete, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.util import await_only

from src.app.cruds.database import get_async_session
from fastapi import Depends

from src.app.models.reservations import Reservation
from src.app.models.tables import Table
from src.app.schemas.reservations import ReservationCreateScheme, ReservationDeleteScheme


async def get_all_reservations(session: AsyncSession) -> list[Reservation]:
    result = await session.execute(select(Reservation))
    return list(result.scalars().all())


async def add_reservation(session: AsyncSession, reservation: ReservationCreateScheme) -> int:
    table_result = await session.execute(select(Table).where(Table.id == reservation.table_id))
    table = table_result.scalars().first()
    reservation = Reservation(
        customer_name=reservation.customer_name,
        table_id=table.id,
        reservation_time=reservation.reservation_time.replace(tzinfo=None),
        duration_minutes=reservation.duration_minutes
    )
    session.add(reservation)
    await session.flush()
    await session.commit()
    return reservation.id


async def del_reservation(session: AsyncSession, reservation_del: ReservationDeleteScheme) -> bool:
    await session.execute(delete(Reservation).where(Reservation.id == reservation_del.id))
    await session.commit()
    return True
