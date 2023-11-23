import tkinter as tk
from builder import *
import time
from auxiliar import guardar_pizza_en_csv
from directorMenus import DirectorMenus


def menuApp():
    # Interfaz gráfica principal
    root = tk.Tk()
    root.title("Pizzeria Pelayo")
    
    combo = DirectorMenus()
    builder = PizzaBuilder()
    combo.builder = builder

    # Función para manejar la selección de la carta
    def seleccionar_pizza():
        eleccion = lista_pizzas.get(lista_pizzas.curselection())
        if eleccion:
            label_estado.config(text=f"Preparando un {eleccion}...")
            root.update()
            time.sleep(2)  # Simular el tiempo de preparación
            if eleccion == "Menu Simple":
                combo.menu_simple()
        
            elif eleccion == "Menu Pareja":
                combo.menu_pareja()
            
            elif eleccion == "Menu del Mar":
                combo.menu_del_mar()
            
            elif eleccion == "Menu Pepperoni":
                combo.menu_pepperoni()

            label_estado.config(text=f"Lista su {eleccion}.")

    # Configuración de la lista de pizzas
    lista_pizzas = tk.Listbox(root)
    lista_pizzas.insert(1, "Menu Simple")
    lista_pizzas.insert(2, "Menu Pareja")
    lista_pizzas.insert(3, "Menu del Mar")
    lista_pizzas.insert(4, "Menu Pepperoni")
    lista_pizzas.pack()

    # Botón para seleccionar pizza de la carta
    boton_seleccionar = tk.Button(root, text="Seleccionar Menu", command=seleccionar_pizza)
    boton_seleccionar.pack()

    # Etiqueta para mostrar el estado de la preparación de la pizza
    label_estado = tk.Label(root, text="")
    label_estado.pack()

    # Inicia la interfaz gráfica
    root.mainloop()