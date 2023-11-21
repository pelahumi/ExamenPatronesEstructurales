import tkinter as tk
from builder import *
import time
from auxiliar import guardar_pizza_en_csv
from directorMenus import DirectorMenus


def pizzaApp():
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
            label_estado.config(text=f"Preparando una pizza de {eleccion}...")
            root.update()
            time.sleep(2)  # Simular el tiempo de preparación
            if eleccion == "Menu Simple":
                combo.menu_simple()
        
            elif eleccion == "Menu Pareja":
                combo.menu_pareja()

            label_estado.config(text=f"Lista su pizza de {eleccion}.")

    # Configuración de la lista de pizzas
    lista_pizzas = tk.Listbox(root)
    lista_pizzas.insert(1, "Menu Simple")
    lista_pizzas.insert(2, "Menu Pareja")
    lista_pizzas.pack()

    # Botón para seleccionar pizza de la carta
    boton_seleccionar = tk.Button(root, text="Seleccionar Menu", command=seleccionar_pizza)
    boton_seleccionar.pack()

    # Etiqueta para mostrar el estado de la preparación de la pizza
    label_estado = tk.Label(root, text="")
    label_estado.pack()

    # Inicia la interfaz gráfica
    root.mainloop()