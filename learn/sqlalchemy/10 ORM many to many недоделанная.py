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
    addresses: Mapped[list["Address"]] = relationship(back_populates="users", uselist=True, secondary="user_address")

    def __repr__(self) -> str:
        return f'User: {self.id=}: {self.name=}: {self.age=}'

class Address(Base):
    __tablename__ = 'addresses'
    email: Mapped[str] = mapped_column(primary_key=True)
    users: Mapped[list["User"]] = relationship(back_populates="addresses", uselist=True, secondary="user_address")


    def __repr__(self) -> str:
        return f'Address: {self.email=}'


class UserAddress(Base):
    __tablename__ = "user_address"
    user_fk = mapped_column(ForeignKey('users.id'))
    address_fk = mapped_column(ForeignKey('addresses.email'))


Base.metadata.create_all(engine)


user = User(id=1, name='Test', age=30)
user2 = User(id=2, name='Test2', age=31)
address = Address(email='test@test.com')
address2 = Address(email='test2@test.com')
# user.addresses.append(address)
# user.addresses.append(address2)
# user2.addresses.append(address)
# user2.addresses.append(address2)
# session.add(user)
# session.add(user2)
# session.commit()
#
# user = session.scalar(select(User))
# print(user)
# print(user.addresses)