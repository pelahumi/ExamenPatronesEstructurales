from Composite.combo import Combo
from Composite.Leafs.bebidas import *
from Composite.Leafs.entrantes import *
from Composite.Leafs.postres import *
from builder import Builder, PizzaBuilder
from auxiliar import guardar_combo

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

        print(self.builder.pizza.nombre)

        menu_simple.añadir_componente(self.builder.pizza)
        menu_simple.añadir_componente(Refresco(3.5))
        menu_simple.añadir_componente(TartaQueso(5))

        nombre = "Menú Simple"
        precio = menu_simple.operation()
        elementos = menu_simple.elementos()

        #guardar_combo(nombre, precio, elementos)

    def menu_pareja(self) -> None:

        menu_pareja = Combo()

        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(Cerveza(3.5))
        menu_pareja.añadir_componente(Agua(3.5))
        menu_pareja.añadir_componente(TartaQueso(5))
        menu_pareja.añadir_componente(Flan(5))

        nombre = "Menú Pareja"
        precio = menu_pareja.operation()
        elementos = menu_pareja.elementos()

        guardar_combo(nombre, precio, elementos)


if __name__ == "__main__":
    director = DirectorMenus()
    builder = PizzaBuilder()
    director.builder = builder

    director.menu_simple()









        

