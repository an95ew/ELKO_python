from sqlalchemy import create_engine
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
session = sessionmaker(engine)

Base = declarative_base()


class Human(Base):

    __tablename__ = "humans"

    id = Column("human_id", Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.create_all(engine)

ivan = Human(id=2, name="Ivan", age=20)

open_session = session()
open_session.add(ivan) # Добавляет класс таблицы, создавая запись в таблице
# Или можно передать список классов таблицы
# open_session.add_all(<list_name>)
open_session.commit()
