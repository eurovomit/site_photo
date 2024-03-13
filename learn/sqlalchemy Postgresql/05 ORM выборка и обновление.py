import asyncio
import datetime
import enum
from typing import Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, text, insert, ForeignKey, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

# ------------- задаем данные базы данных -----------------
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'euro'

DATABASE_URL_asyncpg = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_psycopg = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ------------- создаем движок -----------------
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

# ------------- создаем фабрику сессий -----------------
sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

# ------------- создаем базовый класс для создания моделей -----------------
class Base(DeclarativeBase):
    pass

# ------------- создаем переменные для вставки, которые часто используются -----------------
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
update_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]

# ------------- создаем модель таблицы-----------------
class WorkersORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumesORM(Base):
    __tablename__ = "resumes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at] # вставка переменной, которая часто используется
    updated_at: Mapped[update_at] # вставка переменной, которая часто используется

# ------------- создаем таблицу -----------------
def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

create_tables()

# ------------- вставляем данные в таблицу таблицу -----------------
#синхронный метод
def sync_insert_data():
    with sync_session_factory() as session:
        worker_bobr = WorkersORM(username="Bobr")
        worker_volk = WorkersORM(username="Volf")
        session.add_all([worker_bobr, worker_volk])
        session.commit()

#асинхронный метод
async def async_insert_data():
    async with async_session_factory() as session:
        worker_bobr = WorkersORM(username="Zayc")
        worker_volk = WorkersORM(username="Fox")
        session.add_all([worker_bobr, worker_volk])
        await session.commit()

sync_insert_data()
asyncio.run(async_insert_data())

# ------------- выборка -----------------
def select_workers():
    with sync_session_factory() as session:
        query = select(WorkersORM)
        res = session.execute(query)
        workers = res.all()  # вернуть все строки
        print(f'{workers=}')

select_workers()

# ------------- обновление -----------------
def update_workers(worker_id=2, new_username='Banny'):
    with sync_session_factory() as session:
        worker = session.get(WorkersORM, worker_id)
        worker.username = new_username
        session.commit()

update_workers()