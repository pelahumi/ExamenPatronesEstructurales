from faker import Faker
import sqlite3

def generar_usuarios(n):

    """
    Esta función genera n usuarios aleatorios y los añade a la base de datos de usuarios autorizados
    """

    fake = Faker()

    db = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
    cursor = db.cursor()

    for i in range(n):
        usuario = fake.first_name()
        cursor.execute("INSERT INTO usuarios_autorizados (usuario) VALUES (?)", (usuario,))

    db.commit()
    db.close()  
 


