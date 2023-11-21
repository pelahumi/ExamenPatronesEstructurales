from Composite.combo import Combo
from Composite.Leafs.bebidas import *
from Composite.Leafs.entrantes import *
from Composite.Leafs.postres import *
from builder import Builder, PizzaBuilder

#Clase director
class Director():

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

        print(f"{menu_simple.operation()}")

    def menu_pareja(self) -> None:

        menu_pareja = Combo()

        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(self.builder.pizza)
        menu_pareja.añadir_componente(Cerveza(3.5))
        menu_pareja.añadir_componente(Agua(3.5))
        menu_pareja.añadir_componente(TartaQueso(5))
        menu_pareja.añadir_componente(Flan(5))

        print(f"{menu_pareja.operation()}")


director = Director()
builder = PizzaBuilder()
director.builder = builder

director.menu_simple()
director.menu_pareja()








        

