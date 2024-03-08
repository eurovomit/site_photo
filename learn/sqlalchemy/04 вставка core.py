from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert
from sqlalchemy.dialects import sqlite, postgresql

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("name", String(30)),
    Column("fullname", String())
)

address = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("email_address", String(30)),
    Column("user_id", ForeignKey('users.id'))
)

metadata.create_all(engine)

stmt = insert(user_table).values(name='Alex', fullname='Alex Alex')
sqlite_stmt = stmt.compile(engine, sqlite.dialect())
print(sqlite_stmt)
# INSERT INTO users (name, fullname) VALUES (?, ?)
postgresql_stmt = stmt.compile(engine, postgresql.dialect())
print(postgresql_stmt)
# INSERT INTO users (name, fullname) VALUES (%(name)s, %(fullname)s) RETURNING users.id

with engine.begin() as conn: #type: Connection
    result = conn.execute(sqlite_stmt)
    print(result.inserted_primary_key)
    # (1,)
