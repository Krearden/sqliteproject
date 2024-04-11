from datetime import date

DB_NAME = 'mydb.db'
BP_NAME = 'backup.db'
INSERT_DATA = True

car_brands = ["Lada", "Ford"]

cars = [
    {"owner": "Иванов Иван", "number": "A123BC", "brand_name": "Lada", "year": 2010, "color": "Синий", 
     "mileage": 100000, "price": 300000, "inspection": True, "registration_date": date(2012, 5, 15)},
    {"owner": "Петров Петр", "number": "M777KK", "brand_name": "Lada", "year": 2013, "color": "Зеленый", 
     "mileage": 75000, "price": 250000, "inspection": True, "registration_date": date(2014, 8, 2)},
    {"owner": "Сергеев Сергей", "number": "O888OO", "brand_name": "Ford", "year": 2015, "color": "Черный", 
     "mileage": 50000, "price": 400000, "inspection": False, "registration_date": date(2016, 6, 20)},
    {"owner": "Александров Александр", "number": "P999PP", "brand_name": "Lada", "year": 2018, "color": "Белый", 
     "mileage": 20000, "price": 350000, "inspection": True, "registration_date": date(2019, 4, 15)},
    {"owner": "Николаев Николай", "number": "K555KK", "brand_name": "Ford", "year": 2020, "color": "Серый", 
     "mileage": 10000, "price": 500000, "inspection": True, "registration_date": date(2021, 7, 30)}
]
