import sqlite3

#Creamos la base de datos que contendrá los menús y sus precios

conexion = sqlite3.connect("Samur/DataBase/acceso.db")

cursor = conexion.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS acceso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL,
        modificacion INTEGRER,
        hora_modificacion TEXT
    )"""
)

conexion.commit()
conexion.close()