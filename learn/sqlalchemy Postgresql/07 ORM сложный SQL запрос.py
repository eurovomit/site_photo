import asyncio
import datetime
import enum
from typing import Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, text, insert, ForeignKey, select, cast, \
    func, and_
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, aliased

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
        workers = [
            {"username": "Alex"},  # id 1
            {"username": "Alen"},  # id 2
            {"username": "Artem"},  # id 3
            {"username": "Roman"},  # id 4
            {"username": "Petr"},  # id 5
        ]
        resumes = [
            {"title": "Python Junior Dev", "compensation": 50000, "workload": "fulltime", "worker_id": 1},
            {"title": "Python Dev", "compensation": 150000, "workload": "fulltime", "worker_id": 1},
            {"title": "Python Data", "compensation": 250000, "workload": "parttime", "worker_id": 2},
            {"title": "Data Scientist", "compensation": 300000, "workload": "fulltime", "worker_id": 3},
            {"title": "Python программист", "compensation": 60000, "workload": "fulltime", "worker_id": 3},
            {"title": "Machine Learning Engineer", "compensation": 70000, "workload": "parttime", "worker_id": 3},
            {"title": "Python Data Scientist", "compensation": 80000, "workload": "parttime", "worker_id": 4},
            {"title": "Python Analyst", "compensation": 90000, "workload": "fulltime", "worker_id": 4},
            {"title": "Python Junior Developer", "compensation": 100000, "workload": "fulltime", "worker_id": 5},
        ]
        insert_workers = insert(WorkersORM).values(workers)
        insert_resumes = insert(ResumesORM).values(resumes)
        session.execute(insert_workers)
        session.execute(insert_resumes)
        session.commit()


sync_insert_data()

# ------------- сложный SQL запрос -----------------
def join_cte_subquery_window_func():
    """
    WITH helper2 AS (
        SELECT *, compensation-avg_workload_compensation AS compensation_diff
        FROM
        (SELECT
            w.id,
            w.username,
            r.compensation,
            r.workload,
            avg(r.compensation) OVER (PARTITION BY workload)::int AS avg_workload_compensation
        FROM resumes r
        JOIN workers w ON r.worker_id = w.id) helper1
    )
    SELECT * FROM helper2
    ORDER BY compensation_diff DESC;
    """
    with sync_session_factory() as session:
        r = aliased(ResumesORM) # задаем псевдонимы
        w = aliased(WorkersORM)
        subq = ( # подзапрос
            select(
                r,
                w,
                func.avg(r.compensation).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation"),
            )
            # .select_from(r)
            .join(r, r.worker_id == w.id).subquery("helper1")
        )
        cte = (
            select(
                subq.c.worker_id,
                subq.c.username,
                subq.c.compensation,
                subq.c.workload,
                subq.c.avg_workload_compensation,
                (subq.c.compensation - subq.c.avg_workload_compensation).label("compensation_diff"),
            )
            .cte("helper2")
        )
        query = (
            select(cte)
            .order_by(cte.c.compensation_diff.desc())
        )

        res = session.execute(query)
        result = res.all()
        print(result)
        # print(f"{len(result)=}. {result=}")