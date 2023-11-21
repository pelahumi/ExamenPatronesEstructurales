from Composite.combo import Combo
from Composite.Leafs.bebidas import *
from Composite.Leafs.entrantes import *
from Composite.Leafs.postres import *
from builder import Builder, PizzaBuilder
import sqlite3

#Clase director
class DirectorMenus():

    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    #Menus que están disponibles en la carta de la pizzería
    def menu_simple(self) -> None:

        menu_simple = Combo()

        menu_simple.añadir_componente(self.builder.pizza)
        menu_simple.añadir_componente(Refresco(3.5))
        menu_simple.añadir_componente(TartaQueso(5))

        precio = menu_simple.operation()
        elementos = menu_simple.elementos()

        conexion = sqlite3.connect("Pizzeria/DataBase/menus.db")
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO menus (precio, elementos) VALUES (?, ?)", (precio, elementos))

        conexion.commit()
        conexion.close()

    def menu_pareja(self) -> None:

        menu_pareja = Combo()

        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(Cerveza(3.5))
        menu_pareja.añadir_componente(Agua(3.5))
        menu_pareja.añadir_componente(TartaQueso(5))
        menu_pareja.añadir_componente(Flan(5))

        precio = menu_pareja.operation()
        elementos = menu_pareja.elementos()

        conexion = sqlite3.connect("Pizzeria/DataBase/menus.db")
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO menus (precio, elementos) VALUES (?, ?)", (precio, elementos))

        conexion.commit()
        conexion.close()


director = DirectorMenus()
builder = PizzaBuilder()
director.builder = builder

director.menu_simple()









        

