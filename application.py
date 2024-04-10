import tkinter as tk
from tkinter import ttk
from databaseManager import DatabaseManager
from constants import DB_NAME
from tkcalendar import DateEntry
from datetime import datetime

def create_window():
    window = tk.Tk()
    window.title("Машины")
    window.resizable(False, False)

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Машины')
    tab_control.pack(expand=1, fill='both')

    db_manager = DatabaseManager(f'{DB_NAME}')
    cars = db_manager.getAllCars()

    # Добавляем кнопку "Добавить"
    add_button = tk.Button(tab1, text="Добавить", command=lambda: add_car(db_manager))
    add_button.pack()

    tree = ttk.Treeview(tab1)
    tree["columns"] = ("id", "owner", "number", "brand", "year", "color", "mileage", "price", "inspection", "registration_date")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("id", anchor=tk.W, width=100)
    tree.column("owner", anchor=tk.W, width=100)
    tree.column("number", anchor=tk.W, width=100)
    tree.column("brand", anchor=tk.W, width=100)
    tree.column("year", anchor=tk.W, width=100)
    tree.column("color", anchor=tk.W, width=100)
    tree.column("mileage", anchor=tk.W, width=100)
    tree.column("price", anchor=tk.W, width=100)
    tree.column("inspection", anchor=tk.W, width=100)
    tree.column("registration_date", anchor=tk.W, width=100)

    tree.heading("id", text="ID", anchor=tk.W)
    tree.heading("owner", text="Владелец", anchor=tk.W)
    tree.heading("number", text="Номер", anchor=tk.W)
    tree.heading("brand", text="Марка", anchor=tk.W)
    tree.heading("year", text="Год выпуска", anchor=tk.W)
    tree.heading("color", text="Цвет", anchor=tk.W)
    tree.heading("mileage", text="Пробег", anchor=tk.W)
    tree.heading("price", text="Цена", anchor=tk.W)
    tree.heading("inspection", text="Техосмотр", anchor=tk.W)
    tree.heading("registration_date", text="Дата регистрации", anchor=tk.W)

    for car in cars:
        tree.insert("", "end", values=(car.id, car.owner, car.number, car.brand.brand_name, car.year, car.color, car.mileage, car.price, car.inspection, car.registration_date))

    tree.pack()
    window.mainloop()


def validate_string(input):
    # Проверяем, что ввод состоит только из букв и пробелов
    return all(char.isalpha() or char.isspace() for char in input)

def validate_number(input):
    # Проверяем, что ввод состоит только из цифр
    return all(char.isdigit() for char in input)

def add_car(db_manager):
    add_window = tk.Toplevel()
    add_window.title("Добавить автомобиль")
    add_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем поля для ввода данных
    tk.Label(add_window, text="Владелец").grid(row=0, column=0)
    owner_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_string), "%P"))
    owner_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Номер").grid(row=1, column=0)
    number_entry = tk.Entry(add_window)
    number_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Марка").grid(row=2, column=0)
    brand_names = db_manager.get_all_car_brand_names()
    brand_combobox = ttk.Combobox(add_window, values=brand_names)
    brand_combobox.grid(row=2, column=1)

    tk.Label(add_window, text="Год выпуска").grid(row=3, column=0)
    year_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_number), "%P"))
    year_entry.grid(row=3, column=1)

    tk.Label(add_window, text="Цвет").grid(row=4, column=0)
    color_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_string), "%P"))
    color_entry.grid(row=4, column=1)

    tk.Label(add_window, text="Пробег").grid(row=5, column=0)
    mileage_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_number), "%P"))
    mileage_entry.grid(row=5, column=1)

    tk.Label(add_window, text="Цена").grid(row=6, column=0)
    price_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_number), "%P"))
    price_entry.grid(row=6, column=1)

    tk.Label(add_window, text="Техосмотр").grid(row=7, column=0)
    inspection_combobox = ttk.Combobox(add_window, values=["True", "False"])
    inspection_combobox.grid(row=7, column=1)

    # Дата регистрации
    tk.Label(add_window, text="Дата регистрации").grid(row=8, column=0)
    registration_date_entry = DateEntry(add_window)
    registration_date_entry.grid(row=8, column=1)

    # Создаем кнопку "ОК"
    ok_button = tk.Button(add_window, text="ОК", command=lambda: create_car(db_manager, owner_entry.get(), number_entry.get(), brand_combobox.get(), year_entry.get(), color_entry.get(), mileage_entry.get(), price_entry.get(), inspection_combobox.get() == "True", registration_date_entry.get_date()))
    ok_button.grid(row=9, column=0, columnspan=2)



def create_car(db_manager, owner, number, brand, year, color, mileage, price, inspection, registration_date):
    # Создание нового автомобиля
    db_manager.create_car(owner, number, brand, year, color, mileage, price, inspection, registration_date)
    print("Автомобиль успешно добавлен!")

