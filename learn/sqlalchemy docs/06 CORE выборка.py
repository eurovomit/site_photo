from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine, insert, select, and_, or_, \
    func, union_all, update, bindparam, delete

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
stmt = insert(user_table).values(name="Victoria", fullname="Alexeeva")
compiled = stmt.compile()
print(stmt) # выведет SQL запрос INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)
print(compiled.params) # выведет параметры запроса {'name': 'Victoria', 'fullname': 'Victoria Alexeeva'}

# выполняем скрипт
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

# вставка нескольких строк
with engine.connect() as conn:
    conn.execute(
        insert(user_table),
        [
            {"name": "Maria", "fullname": "Alexeeva"},
            {"name": "Evgenia", "fullname": "Alexeeva"},
            {"name": "Rita", "fullname": "Uvarova"},
        ]
    )
    conn.commit()

# вставка нескольких строк
with engine.connect() as conn:
    conn.execute(
        insert(address_table),
        [
            {"user_id": 1, "email_address": "eurovika@gmail.com"},
            {"user_id": 1, "email_address": "eurovica@gmail.com"},
            {"user_id": 2, "email_address": "euromasha@gmail.com"},
            {"user_id": 3, "email_address": "eurogenya@gmail.com"},
        ]
    )
    conn.commit()

# ============ выборка =============
# выбор всех столбцов
stmt = select(user_table).where(user_table.c.name == "Maria")
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # (2, 'Maria', 'Maria Alexeeva')

# с выбором не всех столбцов
stmt = select(user_table.c.name).where(user_table.c.name == "Maria")
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # ('Maria',)

# с псевдонимом
stmt = select(("Имя: " + user_table.c.name).label("username")).where(user_table.c.name == "Maria")
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username}") # Имя: Maria

# where 2 условия
stmt = select(user_table).where(user_table.c.id > 1).where(user_table.c.id < 3)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # (2, 'Maria', 'Maria Alexeeva')

# where 2 условия в одном where
stmt = select(user_table).where(user_table.c.id > 1, user_table.c.id < 3)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # (2, 'Maria', 'Maria Alexeeva')

# where с оператором and
stmt = select(user_table).where(and_(user_table.c.id > 1, user_table.c.id < 3))
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # (2, 'Maria', 'Maria Alexeeva')

# where с оператором or
stmt = select(user_table).where(or_(user_table.c.id == 1, user_table.c.id == 3))
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row) # (1, 'Victoria', 'Victoria Alexeeva'), (3, 'Evgenia', 'Evgenia Alexeeva')

# from по умолчанию
stmt = select(user_table)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [(1, 'Victoria', 'Alexeeva'), (2, 'Maria', 'Alexeeva'), (3, 'Evgenia', 'Alexeeva')]

# from по умолчанию с выбранными столбцами
stmt = select(user_table.c.name, user_table.c.fullname)
with engine.connect() as conn:
    print(conn.execute(stmt).all())  # [('Victoria', 'Alexeeva'), ('Maria', 'Alexeeva'), ('Evgenia', 'Alexeeva')]

# join_from с явно заданными таблицами
stmt = select(user_table.c.name, address_table.c.email_address).join_from(user_table, address_table)
with engine.connect() as conn:
    print(conn.execute(stmt).all())  # [('Victoria', 'eurovika@gmail.com'), ('Maria', 'euromasha@gmail.com'), ('Evgenia', 'eurogenya@gmail.com')]

# join в нем указывается только вторая таблица
stmt = select(user_table.c.name, address_table.c.email_address).join(address_table)
with engine.connect() as conn:
    print(conn.execute(stmt).all())  # [('Victoria', 'eurovika@gmail.com'), ('Maria', 'euromasha@gmail.com'), ('Evgenia', 'eurogenya@gmail.com')]

# join с указанием обеих таблиц
stmt = select(address_table.c.email_address).select_from(user_table).join(address_table)
with engine.connect() as conn:
    print(conn.execute(stmt).all())  # [('eurovika@gmail.com',), ('euromasha@gmail.com',), ('eurogenya@gmail.com',)]

# join с явно заданным ON
stmt = select(user_table.c.name, address_table.c.email_address).join(address_table, user_table.c.id == address_table.c.user_id)
with engine.connect() as conn:
    print(conn.execute(stmt).all())     # [('Victoria', 'eurovika@gmail.com'),
                                        # ('Victoria', 'eurovica@gmail.com'),
                                        # ('Maria', 'euromasha@gmail.com'),
                                        # ('Evgenia', 'eurogenya@gmail.com')]

# left join
stmt = select(address_table.c.email_address, user_table.c.name).join(user_table, isouter=True)
with engine.connect() as conn:
    print(conn.execute(stmt).all())

# full join
stmt = select(address_table.c.email_address, user_table.c.name).join(user_table, full=True)
with engine.connect() as conn:
    print(conn.execute(stmt).all())     #[('eurovika@gmail.com', 'Victoria'),
                                        # ('eurovica@gmail.com', 'Victoria'),
                                        # ('euromasha@gmail.com', 'Maria'),
                                        # ('eurogenya@gmail.com', 'Evgenia'),
                                        # (None, 'Rita')]

# order by
stmt = select(user_table).order_by(user_table.c.name)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [(3, 'Evgenia', 'Alexeeva'),
                                    # (2, 'Maria', 'Alexeeva'),
                                    # (4, 'Rita', 'Uvarova'),
                                    # (1, 'Victoria', 'Alexeeva')]

# order by desc
stmt = select(user_table).order_by(user_table.c.name.desc())
with engine.connect() as conn:
    print(conn.execute(stmt).all())     # [(1, 'Victoria', 'Alexeeva'),
                                        # (4, 'Rita', 'Uvarova'),
                                        # (2, 'Maria', 'Alexeeva'),
                                        # (3, 'Evgenia', 'Alexeeva')]

# group by
stmt = select(user_table.c.name, func.count(address_table.c.id).label("count"))\
    .join(address_table)\
    .group_by(user_table.c.name)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [('Evgenia', 1), ('Maria', 1), ('Victoria', 2)]

# having
stmt = select(user_table.c.name, func.count(address_table.c.id).label("count"))\
    .join(address_table)\
    .group_by(user_table.c.name)\
    .having(func.count(address_table.c.id) < 2)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [('Evgenia', 1), ('Maria', 1)]

# group by
stmt = select(user_table.c.name, func.count(address_table.c.id).label("count"))\
    .join(address_table)\
    .group_by(user_table.c.name)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [('Evgenia', 1), ('Maria', 1), ('Victoria', 2)]

# использование именований одной и той же таблицы
user_alias_1 = user_table.alias()
user_alias_2 = user_table.alias()
stmt = select(user_alias_1.c.name, user_alias_2.c.name).join_from(
    user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id
)
with engine.connect() as conn:
    print(conn.execute(stmt).all())

# субзапросы
subq = (
    select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
        .group_by(address_table.c.user_id)
        .subquery()
) # это и есть субзапрос, к нему можно обращаться как к таблице, показано далее
print(subq) # SELECT count(address.id) AS count, address.user_id FROM address GROUP BY address.user_id
with engine.connect() as conn:
    print(conn.execute(select(subq)).all()) # [(2, 1), (1, 2), (1, 3)] - число почт у юзера и id юзера
with engine.connect() as conn:
    print(conn.execute(select(subq.c.user_id, subq.c.count)).all()) # [(1, 2), (2, 1), (3, 1)] - наоборот
# их можно джойнить, субзапросы запоминают ключи из своих запросов
stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(user_table, subq)
with engine.connect() as conn:
    print(conn.execute(stmt).all()) # [('Victoria', 'Alexeeva', 2), ('Maria', 'Alexeeva', 1), ('Evgenia', 'Alexeeva', 1)]

# union
stmt1 = select(user_table).where(user_table.c.fullname == "Uvarova")
stmt2 = select(user_table).where(user_table.c.name == "Maria")
u = union_all(stmt1, stmt2)
with engine.connect() as conn:
    print(conn.execute(u).all())

# EXISTS
subq = (select(func.count(address_table.c.id))
        .where(user_table.c.id == address_table.c.user_id)
        .group_by(address_table.c.user_id)
        .having(func.count(address_table.c.id) > 1)
        ).exists()
with engine.connect() as conn:
    result = conn.execute(select(user_table.c.name).where(subq))
    print(result.all()) # [('Victoria',)]

# проверить тип данных
print(func.now().type) # DATETIME

# UPDATE
stmt = (update(user_table).where(user_table.c.name == "Rita").values(fullname="Andropova"))
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
with engine.connect() as conn:
    result = conn.execute(select(user_table).where(user_table.c.name == "Rita"))
    print(result.all())

# UPDATE множественное обновление данных
stmt = (update(user_table).where(user_table.c.name == bindparam("oldname")).values(name=bindparam("newname")))
with engine.begin() as conn:
    res = conn.execute(stmt,
                 [
                     {"oldname": "Victoria", "newname": "Vika"},
                     {"oldname": "Maria", "newname": "Masha"},
                     {"oldname": "Evgenia", "newname": "Genya"},
                 ],
                 )
    print(res.rowcount) # сколько строк изменено
    conn.commit()
with engine.connect() as conn:
    result = conn.execute(select(user_table))
    print(result.all())

# DELETE
stmt = delete(user_table).where(user_table.c.name == "Rita")
with engine.connect() as conn:
    res = conn.execute(stmt)
    print(res.rowcount) # сколько строк удалено
    conn.commit()
with engine.connect() as conn:
    result = conn.execute(select(user_table))
    print(result.all())
