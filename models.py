from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Создание базового класса для моделей
Base = declarative_base()

class CarBrand(Base):
    __tablename__ = "car_brands"
    id = Column(Integer, primary_key=True)
    brand_name = Column(String, unique=True)  # Название марки (уникальное)
    car_count = Column(Integer, default=0)     # Количество автомобилей

    # Связь "один ко многим" с таблицей Car
    cars = relationship("Car", backref="brand")

    def __repr__(self):
        return f"CarBrand(brand_name='{self.brand_name}', car_count={self.car_count})"

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    owner = Column(String)                 # Владелец
    number = Column(String)                # Номер автомобиля
    brand_id = Column(Integer, ForeignKey("car_brands.id"))  # Внешний ключ к таблице CarBrand
    year = Column(Integer)                 # Год выпуска
    color = Column(String)                 # Цвет
    mileage = Column(Integer)              # Пробег
    price = Column(Integer)                # Цена
    inspection = Column(Boolean)            # Пройден ли техосмотр
    registration_date = Column(Date)       # Дата регистрации

    def __repr__(self):
        return f"Car(owner='{self.owner}', number='{self.number}', brand={self.brand})"