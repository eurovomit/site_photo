import asyncio
import datetime
import enum
from typing import Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, text, insert, ForeignKey, select, cast, \
    func, and_
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
        junior = ResumesORM(title="Python Junior Dev", compensation=50000, workload=Workload.fulltime, worker_id=1)
        dev = ResumesORM(title="Python Dev", compensation=150000, workload=Workload.fulltime, worker_id=1)
        eng = ResumesORM(title="Python Data", compensation=250000, workload=Workload.parttime, worker_id=2)
        scient = ResumesORM(title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
        session.add_all([worker_bobr, worker_volk])
        session.commit()

def sync_insert_data1():
    with sync_session_factory() as session:
        junior = ResumesORM(title="Python Junior Dev", compensation=50000, workload=Workload.fulltime, worker_id=1)
        dev = ResumesORM(title="Python Dev", compensation=150000, workload=Workload.fulltime, worker_id=1)
        eng = ResumesORM(title="Python Data", compensation=250000, workload=Workload.parttime, worker_id=2)
        scient = ResumesORM(title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
        session.add_all([junior, dev, eng, scient])
        session.commit()


sync_insert_data()
sync_insert_data1()

# ------------- простой SQL запрос -----------------
def select_from():
    pass


def select_resume_avg_compensation(like_language:str="Python"):
    with sync_session_factory() as session:
        query = \
            select(
                ResumesORM.workload,
                cast(func.avg(ResumesORM.compensation), Integer).label("avg_compensation"), # приводим к int, даем псевдоним
            ).select_from(ResumesORM).filter(and_(ResumesORM.title.contains(like_language), # FROM, WHERE, AND, LIKE
                                                  ResumesORM.compensation > 40000)
                                             ).group_by(ResumesORM.workload)
        print(query.compile(compile_kwargs={"literal_binds": True})) # чтоб посмотреть реальный запрос с числами
        res = session.execute(query)
        result = res.all()
        print(result)

select_resume_avg_compensation()