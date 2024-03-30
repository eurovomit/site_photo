from sqlalchemy import create_engine, text

# =========== создать движок ==============
# echo=True       полное логтрование в консоли
# future=True     совместимость с версией алхимии 2.0
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# =========== вставляем данные =============
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
    conn.commit()

# =========== разбираем объект CursorResult =============
with engine.connect() as conn:
    # объект CursorResult итерируемый, но надо помнить, что перебрать его можно только один раз
    # по сути этот объект содержит строчки из запроса, которые мы можем получить с помощью итераций
    result1 = conn.execute(text("SELECT x, y FROM some_table"))
    # вернется объект <sqlalchemy.engine.cursor.CursorResult object at 0x0000021461C016A0>
    print(result1)

    for row in result1:
        # вернется кортеж из значений x и y (1, 1), (2, 4)
        print(row)
        # можно забрать значения x и y x:1 y:1, x:2 y:4
        print(f"x:{row.x} y:{row.y}")

    # можно сразу так забрать значения
    result2 = conn.execute(text("SELECT x, y FROM some_table"))
    for x, y in result2:
        print(f"x:{x} y:{y}")

    # можно так забрать значения
    result3 = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result3:
        x = row[0]
        y = row[1]
        print(x, y)


# =========== методы объекта CursorResult =============

    # вернет все строки в формате списка кортежей   [(1, 1), (2, 4)]
    result4 = conn.execute(text("SELECT x, y FROM some_table"))
    res = result4.all()
    print(res)

    # вернет все строки в формате списка кортежей для выбранных колонок [(1,), (2,)]
    result5 = conn.execute(text("SELECT x, y FROM some_table"))
    res = result5.columns('y').all()
    print(res)

    # вернет первую строку в формате кортежа (1, 1) или `None`, если ни одна строка не присутствует
    result5 = conn.execute(text("SELECT x, y FROM some_table"))
    res = result5.first()
    print(res)

    # вернет первую строку в формате кортежа (1, 1) или исключение, если присутствует меньше или больше одной строки
    # result6 = conn.execute(text("SELECT x, y FROM some_table"))
    # res = result6.one()
    # print(res)

    # вернет первый элемент первой строки и закроет результирующий набор
    result7 = conn.execute(text("SELECT x, y FROM some_table"))
    res = result7.scalar()
    print(res)

    # вернет итерируемый объект <sqlalchemy.engine.result.ScalarResult object at 0x000002359BA7BBB0> первой строки
    result8 = conn.execute(text("SELECT x, y FROM some_table"))
    res = result8.scalars()
    print(res)
