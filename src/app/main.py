import sys

from fastapi import FastAPI

from src.app.routers.reservations import router as reservations_router
from src.app.routers.tables import router as tables_router


app = FastAPI(
    title='Booking service',
    version='0.1'
)

app.include_router(reservations_router)
app.include_router(tables_router)

