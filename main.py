import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
from models import Base
from constants import DB_NAME, INSERT_DATA, car_brands, cars
from application import create_window
from databaseManager import DatabaseManager
from models import Base, CarBrand, Car
from datetime import date



def create_database(db_file):
    conn = sqlite3.connect(db_file)
    print(f"База данных {db_file} успешно создана!")

def create_tables_if_not_exists(db_file):
    engine = create_engine(f'sqlite:///{db_file}')
    insp = reflection.Inspector.from_engine(engine)
    existing_tables = insp.get_table_names()

    if 'car_brands' not in existing_tables and 'cars' not in existing_tables:
        Base.metadata.create_all(engine)
        print("Таблицы успешно созданы!")
    else:
        print("Таблицы уже существуют!")



if __name__ == "__main__":
    create_database(DB_NAME)
    create_tables_if_not_exists(DB_NAME)
    if INSERT_DATA:
        db_manager = DatabaseManager(DB_NAME)
        db_manager.load_data(car_brands, cars)
    create_window()