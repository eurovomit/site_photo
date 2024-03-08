from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, desc
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



with engine.begin() as conn:
    # запрос с условием
    res1 = conn.execute(select(user_table).where(user_table.c.name == "A1"))
    # запрос с двумя условиями
    res2 = conn.execute(select(user_table).where(user_table.c.name.startswith("A"),
                                                 user_table.c.fullname.contains("3")))
    # запрос с условием или
    res3 = conn.execute(select(user_table).where(or_(user_table.c.name.startswith("A1"),
                                                     user_table.c.fullname.contains("3"))))
    # запрос с условием не на всю таблицу
    res4 = conn.execute(select(user_table.c.id, user_table.c.name).where(or_(user_table.c.name.startswith("A1"),
                                                                             user_table.c.fullname.contains("3"))))
    # запрос с условием IN
    res5 = conn.execute(select(user_table).where(user_table.c.id.in_([1, 2])))
    # вывод в словаре
    res6 = conn.execute(select(user_table).where(user_table.c.id.in_([1, 2])))
    # склейка результата
    res7 = conn.execute(select(user_table.c.id + ' ' + user_table.c.name))
    # даем псевдоним склейке результата
    res8 = conn.execute(select((user_table.c.id + ' ' + user_table.c.name).label('testing')))
    # обращаемся через лейбл в принте
    res9 = conn.execute(select((user_table.c.id + ' ' + user_table.c.name).label('testing')))
    # join
    res10 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join_from(user_table, address))
    # join полная запись
    res11 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join_from(user_table,
                                                                              address,
                                                                              user_table.c.id == address.c.user_id))
    # join ещё один способ
    res12 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address))
    # left join, full join
    res13 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address, isouter=True, full=True))
    # order by
    res14 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address, isouter=True).order_by(user_table.c.id))
    # order by desc
    res15 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address, isouter=True).order_by(desc(user_table.c.id)))
    # то же самое
    res16 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address, isouter=True).order_by(user_table.c.id.desc()))
    # order by по лейблу, group by
    res17 = conn.execute(select(address.c.email_address.label('email'),
                                user_table.c.name.label('testing')).join(address,
                                                                         isouter=True
                                                                         ).order_by(desc("email")
                                                                                    ).group_by("email"
                                                                                               ))

print(res1.all())
print(res2.all())
print(res3.all())
print(res4.all())
print(res5.all())
print(res6.mappings().all())
print(res7.mappings().all())
print(res8.mappings().all())
for res in res9:
    print(res.testing)
print(res10.all())
print(res11.all())
print(res12.all())
print(res15.all())
print(res16.all())
print(res17.all())
