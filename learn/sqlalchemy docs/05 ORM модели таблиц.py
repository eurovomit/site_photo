from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select
from sqlalchemy.orm import relationship, declarative_base, Session
from sqlalchemy.ext.declarative import as_declarative

# =========== создать движок ==============
# echo=True       полное логтрование в консоли
# future=True     совместимость с версией алхимии 2.0
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# ============ создаем таблицы =============
Base.metadata.create_all(engine)

# ============ вставка данных =============
with Session(engine) as session:
    masha = User(name="Maria", fullname="Alexeeva")
    session.add(masha)
    session.commit()

with Session(engine) as session:
    genya = User(name="Evgenia", fullname="Alexeeva")
    vika = User(name="Victoria", fullname="Alexeeva")
    session.add_all([genya, vika])
    session.commit()


# ============ выборка =============
stmt = select(User)
with Session(engine) as session:
    res = session.execute(stmt)
    print(res) # получим объект ChunkedIteratorResult
    for row in res:
        print(row) # получим кортеж классов (User(id=1, name='Maria', fullname='Maria Alexeeva'),)

stmt = select(User.name, User.fullname)
with Session(engine) as session:
    res = session.execute(stmt)
    print(res)  # получим объект ChunkedIteratorResult
    for row in res:
        print(row)  # получим кортеж значений ('Maria', 'Maria Alexeeva')

# с условием where через filter_by
stmt = select(User).filter_by(fullname="Alexeeva", name="Maria")
with Session(engine) as session:
    res = session.execute(stmt)
    print(res)  # получим объект ChunkedIteratorResult
    for row in res:
        print(row)  # получим кортеж классов (User(id=1, name='Maria', fullname='Alexeeva'),)



