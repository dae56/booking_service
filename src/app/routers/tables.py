import sys
from shutil import which

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.cruds.database import get_async_session
from src.app.cruds.tables import get_all_tables, add_table, del_table
from src.app.schemas.tables import TableScheme, TableCreateScheme, TableDeleteScheme

router = APIRouter(
    tags=['tables'],
    prefix='/tables',
)


@router.get('/')
async def get_tables(session: AsyncSession = Depends(get_async_session)) -> list[TableScheme]:
    res = await get_all_tables(session)
    return res


@router.post('/')
async def create_table(table: TableCreateScheme, session: AsyncSession = Depends(get_async_session)):
    return await add_table(session, table)


@router.delete('/{id}')
async def delete_table(id: int, session: AsyncSession = Depends(get_async_session)):
    return await del_table(session, TableDeleteScheme(id=int(id)))