import tkinter as tk
from tkinter import ttk
from databaseManager import DatabaseManager
from constants import DB_NAME

def create_window():
    window = tk.Tk()
    window.title("Машины")

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Машины')
    tab_control.pack(expand=1, fill='both')

    db_manager = DatabaseManager(f'{DB_NAME}')
    cars = db_manager.getAllCars()

    tree = ttk.Treeview(tab1)
    tree["columns"] = ("owner", "number", "brand", "year", "color", "mileage", "price", "inspection", "registration_date")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("owner", anchor=tk.W, width=100)
    tree.column("number", anchor=tk.W, width=100)
    tree.column("brand", anchor=tk.W, width=100)
    tree.column("year", anchor=tk.W, width=100)
    tree.column("color", anchor=tk.W, width=100)
    tree.column("mileage", anchor=tk.W, width=100)
    tree.column("price", anchor=tk.W, width=100)
    tree.column("inspection", anchor=tk.W, width=100)
    tree.column("registration_date", anchor=tk.W, width=100)

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
        tree.insert("", "end", values=(car.owner, car.number, car.brand.brand_name, car.year, car.color, car.mileage, car.price, car.inspection, car.registration_date))

    tree.pack()
    window.mainloop()

