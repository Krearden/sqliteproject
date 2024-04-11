import tkinter as tk
from tkinter import ttk
from databaseManager import DatabaseManager
from constants import DB_NAME
from constants import BP_NAME
from tkcalendar import DateEntry
from datetime import datetime
import os
import sys
import shutil

def backup_db(db_name, backup_name):
    # Создаем резервную копию базы данных путем копирования файла
    shutil.copy2(db_name, backup_name)

def restore_db(backup_name, db_name):
    # Восстанавливаем базу данных из резервной копии
    shutil.copy2(backup_name, db_name)

def restart_program():
    """Перезапускает текущую программу."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_cars_tree(tab, db_manager):
    tree = ttk.Treeview(tab)
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

    update_tree(tree, db_manager)

    return tree

def create_brands_tree(tab, db_manager):
    tree = ttk.Treeview(tab)
    tree["columns"] = ("id", "brand_name", "car_count")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("id", anchor=tk.W, width=100)
    tree.column("brand_name", anchor=tk.W, width=100)
    tree.column("car_count", anchor=tk.W, width=100)

    tree.heading("id", text="ID", anchor=tk.W)
    tree.heading("brand_name", text="Марка", anchor=tk.W)
    tree.heading("car_count", text="Количество автомобилей", anchor=tk.W)

    update_brands_tree(tree, db_manager)

    return tree

def create_window():
    window = tk.Tk()
    window.title("Машины")
    window.resizable(False, True)

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 = ttk.Frame(tab_control)
    tab6 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Машины')
    tab_control.add(tab2, text='Бренды')
    tab_control.add(tab3, text='Лада и Форд')
    tab_control.add(tab4, text='Без техосмотра')
    tab_control.add(tab5, text='Отчет «Автомобили»')
    tab_control.add(tab6, text='Резервное копирование')
    tab_control.pack(expand=1, fill='both')
    
    db_manager = DatabaseManager(f'{DB_NAME}')

    # Вкладка "Машины"
    tree = create_cars_tree(tab1, db_manager)
    add_button = tk.Button(tab1, text="Добавить", command=lambda: add_car(db_manager, tree))
    add_button.pack()
    update_button = tk.Button(tab1, text="Обновить", command=lambda: update_car(db_manager, tree))
    update_button.pack()
    delete_button = tk.Button(tab1, text="Удалить", command=lambda: delete_car(db_manager, tree))
    delete_button.pack()
    updatetab_button = tk.Button(tab1, text="Обновить таблицу", command=lambda: update_tree(tree, db_manager))
    updatetab_button.pack()
    
    
    
    tree.pack(fill='both', expand=True)
    
    # Вкладка "Бренды"
    brands_tree = create_brands_tree(tab2, db_manager)
    add_brand_button = tk.Button(tab2, text="Добавить", command=lambda: add_brand(db_manager, brands_tree))
    add_brand_button.pack()
    update_brand_button = tk.Button(tab2, text="Обновить", command=lambda: update_brand(db_manager, brands_tree))
    update_brand_button.pack()
    delete_brand_button = tk.Button(tab2, text="Удалить", command=lambda: delete_brand(db_manager, brands_tree))
    delete_brand_button.pack()
    updatetab_brand_button = tk.Button(tab2, text="Обновить таблицу", command=lambda: update_brands_tree(brands_tree, db_manager))
    updatetab_brand_button.pack()
    brands_tree.pack(fill='both', expand=True)
    

    # Запрос 1
    # Добавление текста задания
    query_text = "Создать запрос, позволяющий получить номера машин Лада и Форд, зарегистрированных ранее 01.01.2015. Структура запроса: «Владелец», «Номер», «Марка», «Год Выпуска», «Дата Регистрации». Записи отсортировать по дате регистрации."
    query_label = tk.Label(tab3, text=query_text, wraplength=400)
    query_label.pack()

    lada_and_ford_cars_tree = create_lada_and_ford_cars_tree(tab3, db_manager)
    update_query_button = tk.Button(tab3, text="Обновить запрос", command=lambda: update_lada_and_ford_cars_tree(lada_and_ford_cars_tree, db_manager))
    update_query_button.pack()
    lada_and_ford_cars_tree.pack(fill='both', expand=True)


    # Запрос 2
    # Добавление текста задания
    query_text = "Создать запрос, позволяющий получить список владельцев автомобилей, не прошедших техосмотр. Структура запроса: «Владелец», «Номер», «Марка», «Год Выпуска», «Пробег», «Техосмотр», «Дата Регистрации». Записи отсортировать по фамилиям владельцев."
    query_label = tk.Label(tab4, text=query_text, wraplength=400)
    query_label.pack()

    cars_without_inspection_tree = create_cars_without_inspection_tree(tab4, db_manager)
    update_query_button = tk.Button(tab4, text="Обновить запрос", command=lambda: update_cars_without_inspection_tree(cars_without_inspection_tree, db_manager))
    update_query_button.pack()
    cars_without_inspection_tree.pack(fill='both', expand=True)


    #Отчет
    query_text = "Создать отчет «Автомобили». Включить группировку по марке автомобиля."
    query_label = tk.Label(tab5, text=query_text, wraplength=400)
    query_label.pack()

    # Создание раскрывающегося списка брендов
    brand_names = db_manager.get_all_car_brand_names()
    brand_name_var = tk.StringVar(tab5)
    brand_name_var.set(brand_names[0])  # установка первого бренда по умолчанию
    brand_name_dropdown = tk.OptionMenu(tab5, brand_name_var, *brand_names)
    brand_name_dropdown.pack()

    cars_by_brand_tree = create_cars_by_brand_tree(tab5, db_manager)
    update_query_button = tk.Button(tab5, text="Обновить запрос", command=lambda: update_cars_by_brand_tree(cars_by_brand_tree, db_manager, brand_name_var.get()))
    update_query_button.pack()
    cars_by_brand_tree.pack(fill='both', expand=True)


    # Backup functional

    # Кнопка "Создать копию"
    backup_button = tk.Button(tab6, text="Создать копию", command=lambda: backup_db(DB_NAME, BP_NAME))
    backup_button.pack()
    
    # Кнопка "Восстановить из копии"
    restore_button = tk.Button(tab6, text="Восстановить из копии", command=lambda: (restore_db(BP_NAME, DB_NAME), restart_program()))
    restore_button.pack()

    window.mainloop()



def validate_string(input):
    # Проверяем, что ввод состоит только из букв и пробелов
    return all(char.isalpha() or char.isspace() for char in input)

def validate_number(input):
    # Проверяем, что ввод состоит только из цифр
    return all(char.isdigit() for char in input)

def add_car(db_manager, tree):
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
    ok_button = tk.Button(add_window, text="ОК", command=lambda: create_car_and_close_window(db_manager, owner_entry.get(), number_entry.get(), brand_combobox.get(), year_entry.get(), color_entry.get(), mileage_entry.get(), price_entry.get(), inspection_combobox.get() == "True", registration_date_entry.get_date(), add_window, tree))
    ok_button.grid(row=9, column=0, columnspan=2)

def update_car(db_manager, tree):
    update_window = tk.Toplevel()
    update_window.title("Обновить автомобиль")
    update_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем раскрывающийся список со всеми имеющимися идентификаторами машин
    tk.Label(update_window, text="ID автомобиля").grid(row=0, column=0)
    car_ids = db_manager.get_all_car_ids()
    car_id_combobox = ttk.Combobox(update_window, values=car_ids)
    car_id_combobox.grid(row=0, column=1)

    # Создаем поля для ввода данных
    tk.Label(update_window, text="Владелец").grid(row=1, column=0)
    owner_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_string), "%P"))
    owner_entry.grid(row=1, column=1)

    tk.Label(update_window, text="Номер").grid(row=2, column=0)
    number_entry = tk.Entry(update_window)
    number_entry.grid(row=2, column=1)

    tk.Label(update_window, text="Марка").grid(row=3, column=0)
    brand_names = db_manager.get_all_car_brand_names()
    brand_combobox = ttk.Combobox(update_window, values=brand_names)
    brand_combobox.grid(row=3, column=1)

    tk.Label(update_window, text="Год выпуска").grid(row=4, column=0)
    year_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_number), "%P"))
    year_entry.grid(row=4, column=1)

    tk.Label(update_window, text="Цвет").grid(row=5, column=0)
    color_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_string), "%P"))
    color_entry.grid(row=5, column=1)

    tk.Label(update_window, text="Пробег").grid(row=6, column=0)
    mileage_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_number), "%P"))
    mileage_entry.grid(row=6, column=1)

    tk.Label(update_window, text="Цена").grid(row=7, column=0)
    price_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_number), "%P"))
    price_entry.grid(row=7, column=1)

    tk.Label(update_window, text="Техосмотр").grid(row=8, column=0)
    inspection_combobox = ttk.Combobox(update_window, values=["True", "False"])
    inspection_combobox.grid(row=8, column=1)

    # Дата регистрации
    tk.Label(update_window, text="Дата регистрации").grid(row=9, column=0)
    registration_date_entry = DateEntry(update_window)
    registration_date_entry.grid(row=9, column=1)

    # Создаем кнопку "ОК"
    ok_button = tk.Button(update_window, text="ОК", command=lambda: update_car_and_close_window(db_manager, car_id_combobox.get(), owner_entry.get(), number_entry.get(), brand_combobox.get(), year_entry.get(), color_entry.get(), mileage_entry.get(), price_entry.get(), inspection_combobox.get() == "True", registration_date_entry.get_date(), update_window, tree))
    ok_button.grid(row=10, column=0, columnspan=2)

def delete_car(db_manager, tree):
    delete_window = tk.Toplevel()
    delete_window.title("Удалить автомобиль")
    delete_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем раскрывающийся список со всеми имеющимися идентификаторами машин
    tk.Label(delete_window, text="ID автомобиля").grid(row=0, column=0)
    car_ids = db_manager.get_all_car_ids()
    car_id_combobox = ttk.Combobox(delete_window, values=car_ids)
    car_id_combobox.grid(row=0, column=1)

    # Создаем кнопку "Удалить"
    delete_button = tk.Button(delete_window, text="Удалить", command=lambda: delete_car_and_close_window(db_manager, car_id_combobox.get(), delete_window, tree))
    delete_button.grid(row=1, column=0, columnspan=2)

def add_brand(db_manager, tree):
    add_window = tk.Toplevel()
    add_window.title("Добавить бренд")
    add_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем поля для ввода данных
    tk.Label(add_window, text="Название").grid(row=0, column=0)
    name_entry = tk.Entry(add_window, validate="key", validatecommand=(add_window.register(validate_string), "%P"))
    name_entry.grid(row=0, column=1)

    # Создаем кнопку "ОК"
    ok_button = tk.Button(add_window, text="ОК", command=lambda: create_brand_and_close_window(db_manager, name_entry.get(), add_window, tree))
    ok_button.grid(row=9, column=0, columnspan=2)

def update_brand(db_manager, tree):
    update_window = tk.Toplevel()
    update_window.title("Обновить бренд")
    update_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем поля для ввода данных
    tk.Label(update_window, text="Старое название").grid(row=0, column=0)
    old_name_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_string), "%P"))
    old_name_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Новое название").grid(row=1, column=0)
    new_name_entry = tk.Entry(update_window, validate="key", validatecommand=(update_window.register(validate_string), "%P"))
    new_name_entry.grid(row=1, column=1)

    # Создаем кнопку "ОК"
    ok_button = tk.Button(update_window, text="ОК", command=lambda: update_brand_and_close_window(db_manager, old_name_entry.get(), new_name_entry.get(), update_window, tree))
    ok_button.grid(row=9, column=0, columnspan=2)

def delete_brand(db_manager, tree):
    delete_window = tk.Toplevel()
    delete_window.title("Удалить бренд")
    delete_window.resizable(False, False)  # Запретить масштабирование окна

    # Создаем поля для ввода данных
    tk.Label(delete_window, text="Название").grid(row=0, column=0)
    name_entry = tk.Entry(delete_window, validate="key", validatecommand=(delete_window.register(validate_string), "%P"))
    name_entry.grid(row=0, column=1)

    # Создаем кнопку "ОК"
    ok_button = tk.Button(delete_window, text="ОК", command=lambda: delete_brand_and_close_window(db_manager, name_entry.get(), delete_window, tree))
    ok_button.grid(row=9, column=0, columnspan=2)

def delete_brand_and_close_window(db_manager, brand_name, delete_window, tree):
    db_manager.delete_car_brand(brand_name)
    delete_window.destroy()
    update_brands_tree(tree, db_manager)

def update_brand_and_close_window(db_manager, old_brand_name, new_brand_name, update_window, tree):
    db_manager.update_car_brand(old_brand_name, new_brand_name)
    update_window.destroy()
    update_brands_tree(tree, db_manager)

def create_brand_and_close_window(db_manager, brand_name, add_window, tree):
    db_manager.create_car_brand(brand_name)
    add_window.destroy()
    update_brands_tree(tree, db_manager)

def delete_car_and_close_window(db_manager, car_id, delete_window, tree):
    db_manager.delete_car_by_id(car_id)
    delete_window.destroy()
    update_tree(tree, db_manager)

def create_car(db_manager, owner, number, brand, year, color, mileage, price, inspection, registration_date):
    # Создание нового автомобиля
    db_manager.create_car(owner, number, brand, year, color, mileage, price, inspection, registration_date)
    print("Автомобиль успешно добавлен!")

def create_car_and_close_window(db_manager, owner, number, brand, year, color, mileage, price, inspection, registration_date, add_window, tree):
    create_car(db_manager, owner, number, brand, year, color, mileage, price, inspection, registration_date)
    add_window.destroy()
    update_tree(tree, db_manager)

def update_car_and_close_window(db_manager, car_id, owner, number, brand_name, year, color, mileage, price, inspection, registration_date, update_window, tree):
    # Получение объекта CarBrand по имени марки
    brand = db_manager.get_car_brand_by_name(db_manager.session, brand_name)
    if brand is None:
        print(f"Марка автомобиля '{brand_name}' не найдена.")
        return
    db_manager.update_car_by_id(car_id, owner=owner, number=number, brand=brand, year=year, color=color, mileage=mileage, price=price, inspection=inspection, registration_date=registration_date)
    print(f"Автомобиль с ID {car_id} успешно обновлен!")
    update_window.destroy()
    update_tree(tree, db_manager)

def create_lada_and_ford_cars_tree(tab, db_manager):
    tree = ttk.Treeview(tab, show='headings')  # Добавьте здесь
    tree["columns"] = ("Владелец", "Номер", "Марка", "Год Выпуска", "Дата Регистрации")
    for column in tree["columns"]:
        tree.heading(column, text=column)
    update_lada_and_ford_cars_tree(tree, db_manager)
    return tree

def update_lada_and_ford_cars_tree(tree, db_manager):
    for i in tree.get_children():
        tree.delete(i)
    cars = db_manager.get_lada_and_ford_cars()
    for car in cars:
        tree.insert("", "end", values=(car.owner, car.number, car.brand.brand_name, car.year, car.registration_date))

def create_cars_without_inspection_tree(tab, db_manager):
    tree = ttk.Treeview(tab, show='headings')
    tree["columns"] = ("Владелец", "Номер", "Марка", "Год Выпуска", "Пробег", "Техосмотр", "Дата Регистрации")
    for column in tree["columns"]:
        tree.heading(column, text=column)
    update_cars_without_inspection_tree(tree, db_manager)
    return tree

def update_cars_without_inspection_tree(tree, db_manager):
    for i in tree.get_children():
        tree.delete(i)
    cars = db_manager.get_cars_without_inspection()
    for car in cars:
        tree.insert("", "end", values=(car.owner, car.number, car.brand.brand_name, car.year, car.mileage, car.inspection, car.registration_date))

def create_cars_by_brand_tree(tab, db_manager):
    tree = ttk.Treeview(tab, show='headings')
    tree["columns"] = ("Владелец", "Номер", "Марка", "Год Выпуска", "Пробег", "Техосмотр", "Дата Регистрации")
    for column in tree["columns"]:
        tree.heading(column, text=column)
    return tree

def update_cars_by_brand_tree(tree, db_manager, brand_name):
    for i in tree.get_children():
        tree.delete(i)
    cars = db_manager.get_cars_by_brand(brand_name)
    for car in cars:
        tree.insert("", "end", values=(car.owner, car.number, car.brand.brand_name, car.year, car.mileage, car.inspection, car.registration_date))

def update_tree(tree, db_manager):
    # Очистка дерева
    for i in tree.get_children():
        tree.delete(i)
    # Добавление новых данных
    cars = db_manager.getAllCars()
    for car in cars:
        if car.brand is not None:
            tree.insert("", "end", values=(car.id, car.owner, car.number, car.brand.brand_name, car.year, car.color, car.mileage, car.price, car.inspection, car.registration_date))

def update_brands_tree(tree, db_manager):
    # Очистка дерева
    for i in tree.get_children():
        tree.delete(i)
    # Добавление новых данных
    brands = db_manager.get_all_car_brands()
    for brand in brands:
        tree.insert("", "end", values=(brand.id, brand.brand_name, brand.car_count))