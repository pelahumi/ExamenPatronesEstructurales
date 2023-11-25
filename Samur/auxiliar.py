import sqlite3

db = sqlite3.connect("Samur/DataBase/acceso.db")
cursor = db.cursor()

def usuario_check(usuario):
    cursor.execute("SELECT usuario FROM acceso WHERE usuario = ?", (usuario,))
    if cursor.fetchone():
        return True
    else:
        return False