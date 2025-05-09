from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os


load_dotenv()

engine = create_async_engine(f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
async_session = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
