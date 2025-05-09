import asyncio

from sqlalchemy import select, table, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.cruds.database import get_async_session

from src.app.models.reservations import Reservation
from src.app.models.tables import Table
from src.app.schemas.tables import TableCreateScheme, TableDeleteScheme


async def get_all_tables(session: AsyncSession) -> list[Table]:
    result = await session.execute(select(Table))
    return list(result.scalars().all())


async def add_table(session: AsyncSession, table: TableCreateScheme) -> int:
    table = Table(
        name=table.name,
        seats=table.seats,
        location=table.location,
    )
    session.add(table)
    await session.flush()
    await session.commit()
    return table.id


async def del_table(session: AsyncSession, table_del: TableDeleteScheme) -> int:
    await session.execute(update(Reservation).where(Reservation.table_id == table_del.id).values(table_id=None))
    await session.execute(delete(Table).where(Table.id == table_del.id))
    await session.commit()
    return True
