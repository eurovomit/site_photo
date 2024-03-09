from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select, inspect
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped, Session, DeclarativeBase, relationship

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

session = Session(engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    addresses: Mapped[list["Address"]] = relationship(back_populates="user", uselist=True)

    def __repr__(self) -> str:
        return f'User: {self.id=}: {self.name=}: {self.age=}'

class Address(Base):
    __tablename__ = 'addresses'
    email: Mapped[str] = mapped_column(primary_key=True)
    user: Mapped["User"] = relationship(back_populates="addresses", uselist=False)
    user_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Address: {self.email=}: {self.user_fk=}'


Base.metadata.create_all(engine)


user = User(id=1, name='Test', age=30)
address = Address(email='test@test.com')
address2 = Address(email='test2@test.com')
user.addresses.append(address)
user.addresses.append(address2)
session.add(user)
session.commit()


# users = session.scalars(select(User)).all()
# addresses = session.scalars(select(Address)).all()
# print(users)
# print(addresses)

user = session.scalar(select(User))
print(user)
print(user.addresses)