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
    cars = relationship("Car", back_populates="brand")

class Car (Base):
    __tablename__ = 'cars'

    def __init__(self, *args):
        self.__base__(*args)
        self.human = None

    car_id = Column(Integer, primary_key=True)
    color = Column(String(25))
    brand_fk = Column(Integer, ForeignKey('car_brands.brand_id'))
    brand = relationship("CarBrand", back_populates='cars')

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


Base.metadata.create_all(engine)

audi = CarBrand(brand_id=1, brand_name='Audi')
bmw = CarBrand(brand_id=2, brand_name='BMW')
mercedes = CarBrand(brand_id=3, brand_name='Mercedes')

brands = [audi, bmw, mercedes]

audi1 = Car(car_id=1, color='White', brand_fk=1)
bmw1 = Car(car_id=2, color='Black', brand_fk=2)
mercedes1 = Car(car_id=3, color='Blue', brand_fk=3)

cars = [audi1, bmw1, mercedes1]

open_session = session()

result_all = open_session.query(Car).all()
for car in result_all:
    print(car)

result_first = open_session.query(Car).first()
print(result_first)

result_get_by_id = open_session.query(Car).get(2)
print(result_get_by_id)

# res = Car.changeColor(id=2, wish_color="Изменён")
# print(res)

cars_result = open_session.query(Car).filter(and_(Car.car_id > 0,
                                                  Car.brand.has(CarBrand.brand_name != "BMW")))

for car in cars_result:
    print(car)


brands_result = open_session.query(CarBrand).get(1)
print(brands_result.cars)
for car in brands_result.cars:
    print(car.color)
