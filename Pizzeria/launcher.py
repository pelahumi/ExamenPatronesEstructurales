from builder import PizzaBuilder
from director import Pizzeria
import time
from auxiliar import guardar_pizza_en_csv, validator
from directorMenus import DirectorMenus

def launcher():

    """
    Función que ejecuta el programa por la terminal
    """

    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder
    combo = DirectorMenus()

    #Declaramos una lista inmutable para mostrar las pizzas de la carta
    CARTA = ["Jamón y queso", "Pepperoni", "Hawaiana", "Vegana", "Especial"]


    print("Bienvenido a la Pizzeria Pelayo, ¿Quiere ver nuestra carta o prefiere una pizza personalizada?:")
    print("1. Carta")
    print("2. Personalizada")
    print("3. Menu")
    opcion = str(input("Introduzca el número de la opción que desea: "))

    if opcion == "1":
        print("Carta:")
        for i in CARTA:
            print(i)

        eleccion = str(input("¿Qué pizza desea pedir?: "))

        while not validator(eleccion):
            print("La pizza que ha elegido no está en la carta, por favor, elija otra.")
            eleccion = input("¿Qué pizza desea pedir?: ")

        print("Preparando una pizza de {}...".format(eleccion))

        if eleccion == "Jamón y queso":
            pizzeria.pizza_jamon_queso()
        
        elif eleccion == "Pepperoni":
            pizzeria.pizza_pepperoni()
        
        elif eleccion == "Hawaiana":
            pizzeria.pizza_hawaiana()
        
        elif eleccion == "Vegana":
            pizzeria.pizza_vegana()
        
        elif eleccion == "Especial":
            pizzeria.pizza_especial()
        
        time.sleep(2)
        ingredientes = builder.pizza.guardar_ingredientes()
        guardar_pizza_en_csv(eleccion, ingredientes)
        print("Lista su pizza de {}.".format(eleccion))

    elif opcion == "2":
        pizzeria.personalizada()
        print("Preparando su pizza...")
        time.sleep(2)
        ingredientes = builder.pizza.guardar_ingredientes()
        guardar_pizza_en_csv("Personalizada", ingredientes)
        print("Lista su pizza personalizada.")

    elif opcion == "3":
        print("Menús:")
        print("1. Menú simple")
        print("2. Menú pareja")
        menu = str(input("¿Qué menú desea pedir?: "))

        while not validator(menu):
            print("El menú que ha elegido no está en la carta, por favor, elija otro.")
            menu = input("¿Qué menú desea pedir?: ")

        if menu == "1":
            combo.menu_simple()
        
        elif menu == "2":
            combo.menu_pareja()
        
        time.sleep(2)
        print("Listo su menú.")

   