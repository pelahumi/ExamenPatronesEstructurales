import csv
import pandas as pd
import sqlite3

def guardar_pizza_en_csv(nombre_pizza, ingredientes):

    """
    Función que guarda las pizzas y sus ingredientes en un fichero csv -> pizzasDB.csv
    """

    # Nombre del archivo CSV en el que se guardarán las pizzas
    archivo_csv = 'Pizzeria/DataBase/pizzasDB.csv'

    # Abre el archivo en modo de escritura
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        # Escribe los detalles de la pizza en el archivo
        writer.writerow([nombre_pizza, ingredientes])

def validator(seleccion):

    """
    Función que valida si el elemento o pizza escogida por el usuario está en la base de datos de la pizzería -> pizzeriaDB.csv
    """

    data = pd.read_csv("Pizzeria/DataBase/pizzeriaDB.csv", sep=';')
    if str(seleccion) in data.values:
        return True
    else:
        return False
    

def guardar_combo(precio, elementos):

    """
    Función que guarda los combos y sus elementos en la base de datos de menus -> menusDB.csv
    """

    #Abrimos conexion con la base de datos
    conexion = sqlite3.connect("Pizzeria/DataBase/menus.db")

    cursor = conexion.cursor()

    #Añadimos los elementos y el precion a la base de datos
    cursor.execute("INSERT INTO menus (precio, elementos) VALUES (?, ?)", (precio, elementos))

    #Guardamos los cambios y cerramos la conexion
    conexion.commit()
    conexion.close()

        