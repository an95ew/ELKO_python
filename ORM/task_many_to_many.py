from sqlalchemy import create_engine, ForeignKey, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Table, Column
from sqlalchemy import String, Integer


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
session = sessionmaker(engine)

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


Base.metadata.create_all(engine)

customer1 = RozetkaCustomer(customer_name='Ted')
customer2 = RozetkaCustomer(customer_name='Brad')
customer3 = RozetkaCustomer(customer_name='Vlad')

ware1 = RozetkaWare(ware_name='Iphone 11 Pro')
ware2 = RozetkaWare(ware_name='Львівське Темне 50л')
ware3 = RozetkaWare(ware_name='Шкарпетки Житомирські')
ware4 = RozetkaWare(ware_name='AirPods Pro')


customer1.wares.append(ware1)
customer1.wares.append(ware4)
customer2.wares = [ware2]
customer3.wares = [ware3]

opened_session = session()
opened_session.add(ware1)
opened_session.add(ware2)
opened_session.add(ware3)
opened_session.add(ware4)
opened_session.add(customer1)
opened_session.add(customer2)
opened_session.add(customer3)

opened_session.commit()
