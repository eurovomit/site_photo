from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, text, insert

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

metadata_obj = MetaData()

# ------------- задаем таблицу -----------------
workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)

# ------------- создаем таблицу -----------------
def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

create_tables()

# ------------- вставляем данные -----------------
def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volf"}
            ]
        )
        conn.execute(stmt)
        conn.commit()

insert_data()