import asyncio

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy import Table, Column, select
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey


Base = declarative_base()

class RozetkaCustomer (Base):
    __tablename__ = 'rozetka_customers'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(50))

    wares = relationship('RozetkaWare', secondary='rozetka_orders')


class RozetkaWare (Base):
    __tablename__ = 'rozetka_wares'

    ware_id = Column(Integer, primary_key=True)
    ware_name = Column(String(50))

    customers = relationship('RozetkaCustomer', secondary='rozetka_orders')


class RozetkaOrder (Base):
    __tablename__ = 'rozetka_orders'

    order_id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("rozetka_customers.customer_id"))
    ware_id = Column(Integer, ForeignKey("rozetka_wares.ware_id"))


# async def create_tables():
#     engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
#     #
#     # async with engine.begin() as connection:
#     #     pass
#
#     async with AsyncSession(engine) as session:
#         async with session.begin():
#             customer = RozetkaCustomer(name="Andrew")
#             session.add(customer)


async def select_customers():
    engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

    async with AsyncSession(engine) as session:
        async with session.begin():
            customers = await session.execute(select(RozetkaCustomer))
            for customer in customers:
                print(customer)


# async def select_ware():
#     engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
#
#     async with AsyncSession(engine) as session:
#         async with session.begin():
#             customers = await session.execute(select())
#             for customer in customers:
#                 print(customer.name)

asyncio.run(select_customers())
