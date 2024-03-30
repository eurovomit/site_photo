from sqlalchemy import create_engine, text

# =========== создать движок ==============
# echo=True       полное логтрование в консоли
# future=True     совместимость с версией алхимии 2.0
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    # отдает объект <sqlalchemy.engine.cursor.CursorResult object at 0x0000019762B816A0>
    print(result)
    # отдает список кортежей [('hello world',)]
    print(result.all())
