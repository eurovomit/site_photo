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
    result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), [{"y": 2}])
    for row in result:
        print(f"x:{row.x} y:{row.y}") # x:2 y:4
