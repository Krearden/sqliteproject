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
    
    def update_car_brand(self, brand_name, new_brand_name):
        """Обновляет название марки автомобиля."""
        session = self.session
        brand = session.query(CarBrand).filter(CarBrand.brand_name == brand_name).first()
        if brand is not None:
            brand.brand_name = new_brand_name
            session.commit()
        else:
            print("Марка автомобиля с таким названием не найдена.")

    def delete_car_brand(self, brand_name):
        """Удаляет марку автомобиля."""
        session = self.session
        brand = session.query(CarBrand).filter(CarBrand.brand_name == brand_name).first()
        if brand is not None:
            session.delete(brand)
            session.commit()
        else:
            print("Марка автомобиля с таким названием не найдена.")

    def update_car(self, number, **kwargs):
        """Обновляет информацию об автомобиле."""
        session = self.session
        car = session.query(Car).filter(Car.number == number).first()
        if car is not None:
            for key, value in kwargs.items():
                if hasattr(car, key):
                    setattr(car, key, value)
            session.commit()
        else:
            print("Автомобиль с таким номером не найден.")

    def delete_car(self, number):
        """Удаляет автомобиль."""
        session = self.session
        car = session.query(Car).filter(Car.number == number).first()
        if car is not None:
            session.delete(car)
            session.commit()
        else:
            print("Автомобиль с таким номером не найден.")

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
    
    def get_all_car_brands(self):
        """Возвращает все марки автомобилей."""
        session = self.session
        car_brands = session.query(CarBrand).all()
        return car_brands

    def get_all_car_brand_names(self):
        """Возвращает имена всех марок автомобилей."""
        session = self.session
        car_brand_names = [brand.brand_name for brand in session.query(CarBrand).all()]
        return car_brand_names
    
    def get_all_car_ids(self):
        """Возвращает все уникальные ID автомобилей."""
        session = self.session
        car_ids = [car.id for car in session.query(Car).all()]
        return car_ids
    
    def delete_car_by_id(self, car_id):
        """Удаляет автомобиль по ID."""
        session = self.session
        car = session.query(Car).filter(Car.id == car_id).first()
        if car is not None:
            session.delete(car)
            session.commit()
            print(f"Автомобиль с ID {car_id} успешно удален!")
        else:
            print(f"Автомобиль с ID {car_id} не найден.")
    
    def update_car_by_id(self, car_id, **kwargs):
        """Обновляет автомобиль по ID."""
        session = self.session
        car = session.query(Car).filter(Car.id == car_id).first()
        if car is not None:
            for key, value in kwargs.items():
                if hasattr(car, key):
                    setattr(car, key, value)
            session.commit()
            print(f"Автомобиль с ID {car_id} успешно обновлен!")
        else:
            print(f"Автомобиль с ID {car_id} не найден.")





