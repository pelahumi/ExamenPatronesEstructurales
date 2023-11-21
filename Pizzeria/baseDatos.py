import sqlite3

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
