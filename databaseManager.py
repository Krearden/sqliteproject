from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models import CarBrand, Car


class DatabaseManager:
    def __init__(self, db_file):
        self.engine = create_engine(f'sqlite:///{db_file}')
        self.session = sessionmaker(bind=self.engine)()
    
    def __del__(self):
        self.session.close()

    def create_car_brand(self, brand_name):
        session = self.session
        brand = session.query(CarBrand).filter(CarBrand.brand_name == brand_name).first()
        if brand is None:
            brand = CarBrand(brand_name=brand_name)
            session.add(brand)
            session.commit()
        return brand

    
    def create_car(self, owner, number, brand_name, year, color, mileage, price, inspection, registration_date):
        """Создает новый автомобиль, если он еще не существует."""
        session = self.session
        brand = self.get_car_brand_by_name(session, brand_name)
        car = session.query(Car).filter(Car.number == number).first()
        if car is None:
            car = Car(owner=owner, number=number, brand=brand, year=year, color=color, mileage=mileage,
                    price=price, inspection=inspection, registration_date=registration_date)
            session.add(car)
            session.commit()
            brand.car_count += 1  # Увеличиваем количество автомобилей для марки
            session.commit()
        else:
            print("Автомобиль с таким номером уже существует в базе данных.")

    
    def get_car_brand_by_name(self, session, brand_name):
        """Возвращает марку автомобиля по названию."""
        return session.query(CarBrand).filter(CarBrand.brand_name == brand_name).first()
    
    def load_data(self, car_brands, cars):
        for brand_name in car_brands:
            self.create_car_brand(brand_name)
        for car in cars:
            self.create_car(**car)
    
    def getAllCars(self):
        session = self.session
        cars = session.query(Car).all()
        return cars
