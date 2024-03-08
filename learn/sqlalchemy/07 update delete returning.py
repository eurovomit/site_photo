from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, desc, \
    update, bindparam, delete
from sqlalchemy.dialects import sqlite, postgresql
from sqlalchemy.sql.operators import or_
from sqlalchemy.testing import in_

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


with engine.begin() as conn:
    conn.execute(
        stmt_wo_values,
        [
            {"name": "A1", "fullname": "A1 A1"},
            {"name": "A2", "fullname": "A2 A2"},
            {"name": "A3", "fullname": "A3 A3"},
        ]
    )
    conn.execute(
        insert(address),
        [
            {"email_address": "test1@test.com", "user_id": 1},
            {"email_address": "test2@test.com", "user_id": 2},
            {"email_address": "test3@test.com", "user_id": 3}
        ]
    )


# update
with engine.begin() as conn:
    conn.execute(update(user_table).where(user_table.c.id == 1).values(name="A111"))
    print(conn.execute(select(user_table)).all())

# update через переменные
with engine.begin() as conn:
    stmt = update(user_table).where(user_table.c.name == bindparam("old")).values(name=bindparam("new"))
    conn.execute(
        stmt,
        [
            {"old": "A2", "new": "A222"},
            {"old": "A3", "new": "A333"},
        ]
    )
    print(conn.execute(select(user_table)).all())


# delete
with engine.begin() as conn:
    conn.execute(delete(user_table).where(user_table.c.id == 1))
    print(conn.execute(select(user_table)).all())

# delete по другой таблице, не поддерживается в sqlite
with engine.begin() as conn:
    delete_stmt = (
        delete(user_table)
        .where(user_table.c.id == address.c.user_id)
        .where(address.c.email_address == "test3@test.com")
    )
    print(delete_stmt.compile(dialect=postgresql.dialect()))


# delete сколько строк удалили
with engine.begin() as conn:
    delete_stmt = (
        delete(user_table)
        .where(user_table.c.id == 3)
    )
    res = conn.execute(delete_stmt)
    print(res.rowcount)


# возвращаем параметры удаленных строк
with engine.begin() as conn:
    delete_stmt = (
        delete(user_table)
        .where(user_table.c.id == 2)
        .returning(user_table.c.name)
    )
    res = conn.execute(delete_stmt).scalars().all()
    print(res)