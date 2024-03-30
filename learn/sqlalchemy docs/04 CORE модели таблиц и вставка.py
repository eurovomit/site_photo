from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine, insert

# =========== создать движок ==============
# echo=True       полное логтрование в консоли
# future=True     совместимость с версией алхимии 2.0
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# создаем объект метадаты
metadata_obj = MetaData()

# ============ создаем модели таблиц =============
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String)
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False)
)

# создаем таблицы
metadata_obj.create_all(engine)

# ================ вставка данных ====================
stmt = insert(user_table).values(name="Victoria", fullname="Victoria Alexeeva")
compiled = stmt.compile()
print(stmt) # выведет SQL запрос INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)
print(compiled.params) # выведет параметры запроса {'name': 'Victoria', 'fullname': 'Victoria Alexeeva'}

# выполняем скрипт
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

# вставка нескольких строк
with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "Maria", "fullname": "Maria Alexeeva"},
            {"name": "Evgenia", "fullname": "Evgenia Alexeeva"},
        ]
    )
    conn.commit()