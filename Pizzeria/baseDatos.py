import sqlite3

#Creamos la base de datos que contendrá los menús y sus precios

conexion = sqlite3.connect("Pizzeria/DataBase/menus.db")

cursor = conexion.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS menus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        precio INTEGER NOT NULL,
        elementos TEXT NOT NULL
    )"""
)

conexion.commit()
conexion.close()
