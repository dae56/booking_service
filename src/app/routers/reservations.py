from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.cruds.database import get_async_session
from src.app.cruds.reservations import get_all_reservations, add_reservation, del_reservation
from src.app.models.reservations import Reservation
from src.app.models.tables import Table
from src.app.schemas.reservations import ReservationScheme, ReservationCreateScheme, ReservationDeleteScheme

router = APIRouter(
    tags=['reservations'],
    prefix='/reservations',
)


@router.get('/')
async def get_reservations(session: AsyncSession = Depends(get_async_session)) -> list[ReservationScheme]:
    res = await get_all_reservations(session)
    return res


@router.post('/')
async def create_reservations(reservation: ReservationCreateScheme, session: AsyncSession = Depends(get_async_session)):
    return await add_reservation(session, reservation)


@router.delete('/{id}')
async def delete_reservations(id: int, session: AsyncSession = Depends(get_async_session)):
    return await del_reservation(session, ReservationDeleteScheme(id=int(id)))
