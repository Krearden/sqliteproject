from datetime import date

DB_NAME = 'mydb.db'
INSERT_DATA = True

car_brands = ["Lada", "Ford"]

cars = [
    {"owner": "Иванов Иван", "number": "A123BC", "brand_name": "Lada", "year": 2010, "color": "Синий", 
     "mileage": 100000, "price": 300000, "inspection": True, "registration_date": date(2012, 5, 15)},
    {"owner": "Петров Петр", "number": "M777KK", "brand_name": "Lada", "year": 2013, "color": "Зеленый", 
     "mileage": 75000, "price": 250000, "inspection": True, "registration_date": date(2014, 8, 2)}
]