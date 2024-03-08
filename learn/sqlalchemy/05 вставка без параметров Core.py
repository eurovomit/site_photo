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
stmt_wo_values = insert(user_table)
sqlite_stmt = stmt.compile(engine, sqlite.dialect())
postgresql_stmt = stmt.compile(engine, postgresql.dialect())


with engine.begin() as conn:  # type: Connection
    result = conn.execute(
        stmt_wo_values,
        [
            {"name": "A1", "fullname": "A1 A1"},
            {"name": "A2", "fullname": "A2 A2"},
            {"name": "A3", "fullname": "A3 A3"},
        ]
    )

