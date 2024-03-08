from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello, world!'"))
    # print(result)
        # < sqlalchemy.engine.cursor.CursorResult object at 0x000001F41E1E16A0 >
    # print(result.all())
        # [('hello, world!',)]
    # print(result.scalar())
        # Получает первый столбец первой строки и закрывает набор результатов.
        # hello, world!
    # print(result.scalars().all())
        # ['hello, world!']
    # print(result.scalar_one())
        # Возвращает ровно один скалярный результат или вызывает исключение
    # print(result.scalar_one_or_none())
        # Возвращает ровно один скалярный результат или ``None``.
    # print(result.first())
        # Получает первую строку или ``None``, если строк нет.
