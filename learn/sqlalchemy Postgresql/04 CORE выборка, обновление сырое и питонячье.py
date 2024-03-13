from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, text, insert, select, update

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

# =========================== выборка данных ===============================
def select_workers():
    with sync_engine.connect() as conn:
        query = select(workers_table)
        res = conn.execute(query)
        workers = res.all()                 # вернуть все строки
        # res = conn.execute(query)
        # workers = res.first()               # вернуть первую строку
        # res = conn.execute(query)
        # workers = res.one()                 # вернуть одну строку, если их больше, то ошибка
        # res = conn.execute(query)
        # workers = res.one_or_none()         # не понятно пока
        print(f'{workers=}')

# =========================== обновление данных ===============================
# сырой запрос
def update_workers1(worker_id:int=2, new_username:str="Fox1"):
    with sync_engine.connect() as conn:
        stmt = text("UPDATE workers SET username=:username WHERE id=:id")
        stmt = stmt.bindparams(username=new_username, id=worker_id)
        conn.execute(stmt)
        conn.commit()


# питонячий запрос
def update_workers2(worker_id:int=2, new_username:str="Fox3"):
    with sync_engine.connect() as conn:
        stmt = update(workers_table).values(username=new_username).where(workers_table.c.id==worker_id)
        # stmt = update(workers_table).values(username=new_username).filter_by(id=worker_id)  # то же самое
        conn.execute(stmt)
        conn.commit()



select_workers()
update_workers1()
update_workers2()