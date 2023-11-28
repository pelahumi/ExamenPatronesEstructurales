import sqlite3

#Creamos la base de datos que contendrá los menús y sus precios

conexion = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")

cursor = conexion.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS usuarios_autorizados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL
    )"""
)

conexion.commit()
conexion.close()


"""conexion = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM usuarios_autorizados")

conexion.commit()
conexion.close()"""