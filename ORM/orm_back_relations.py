from sqlalchemy import create_engine, ForeignKey, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Table, Column
from sqlalchemy import String, Integer


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
session = sessionmaker(engine)

Base = declarative_base()


class CarBrand (Base):
    __tablename__ = 'car_brands'

    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(String(25))

class Car (Base):
    __tablename__ = 'cars'
    #
    # def __init__(self, color):
    #     self.__base__(color)
    #     self.brand = None

    car_id = Column(Integer, primary_key=True)
    color = Column(String(25))
    brand_fk = Column(Integer, ForeignKey('car_brands.brand_id'))
    brand = relationship("CarBrand", backref='brand')

    def __str__ (self):
        return f"Цвет - {self.color}.\n" \
               f"Марка - {self.brand.brand_name}."

    @staticmethod
    def changeColor (id: int, wish_color: str):
        open_session = session()
        car = open_session.query(Car).get(id)
        car.color = wish_color
        open_session.add(car)
        open_session.commit()
        return (f"У {car.brand.brand_name} цвет успешно изменён на {wish_color}!")


car = Car(color = "Yellow")
ford = CarBrand(brand_name="Ford")
car.brand = ford
opened_session = session()
opened_session.add(car)
opened_session.commit()
