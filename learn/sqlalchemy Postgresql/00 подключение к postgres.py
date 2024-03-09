import asyncio

from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'euro'

DATABASE_URL_asyncpg = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_psycopg = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# обычный движок
sync_engine = create_engine(
    url=DATABASE_URL_psycopg,
    echo=False
)

# асинхронный движок
async_engine = create_async_engine(
    url=DATABASE_URL_asyncpg,
    echo=False
)

with sync_engine.connect() as conn:
    res = conn.execute(text('select version()'))
    print(f'{res.first()}')


async def get_ver():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('select version()'))
        print(f'{res.first()}')

asyncio.run(get_ver())