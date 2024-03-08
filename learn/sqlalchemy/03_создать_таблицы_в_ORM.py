from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped, Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(primary_key=True)

    # чтоб имя таблицы было по классу, только в нижнем регистре
    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = 'users'
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()


class AddressModel(AbstractModel):
    __tablename__ = 'addresses'
    email: Mapped[str] = mapped_column(nullable=False)
    user_id = mapped_column(ForeignKey('users.id'))


with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)
        user = UserModel(name='Alex', fullname='Alex Alexeev')
        session.add(user)
    with session.begin():
        res = session.execute(select(UserModel).where(UserModel.id == 1))
        print(res.scalar())