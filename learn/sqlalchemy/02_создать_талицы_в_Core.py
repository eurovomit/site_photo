from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("fullname", String),
)

address = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey('users.id')),
    Column("email", String, nullable=False),
)

print(user_table.c.keys())
    # ['id', 'name', 'fullname']

# создать все таблицы
metadata.create_all(engine)

# удалить все таблицы
# metadata.drop_all(engine)