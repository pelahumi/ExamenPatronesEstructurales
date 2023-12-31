from Composite.combo import Combo
from Composite.Leafs.bebidas import *
from Composite.Leafs.entrantes import *
from Composite.Leafs.postres import *
from builder import Builder, PizzaBuilder, Pizza
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

        print(self.builder.pizza.set_nombre("Pizza Simple"))

        menu_simple.añadir_componente(self.builder.pizza)
        menu_simple.añadir_componente(Refresco(3.5))
        menu_simple.añadir_componente(TartaQueso(5))

        nombre = "Menú Simple"
        precio = menu_simple.operation()
        elementos = menu_simple.elementos()

        guardar_combo(nombre, precio, elementos)
    
    def menu_pepperoni(self) -> None:
            
        menu_pepperoni = Combo()
    
        pizza = self.builder.pizza
        pizza.set_nombre("Pizza Pepperoni")
    
        menu_pepperoni.añadir_componente(pizza)
        menu_pepperoni.añadir_componente(Refresco(3.5))
        menu_pepperoni.añadir_componente(TartaQueso(5))
    
        nombre = "Menú Pepperoni"
        precio = menu_pepperoni.operation()
        elementos = menu_pepperoni.elementos()
    
        guardar_combo(nombre, precio, elementos)
    
    def menu_del_mar(self) -> None:
        
            menu_del_mar = Combo()
        
            pizza = self.builder.pizza
            pizza.set_nombre("Pizza Hawaiana")
        
            menu_del_mar.añadir_componente(pizza)
            menu_del_mar.añadir_componente(Agua(2))
            menu_del_mar.añadir_componente(Flan(4.5))
        
            nombre = "Menú del Mar"
            precio = menu_del_mar.operation()
            elementos = menu_del_mar.elementos()
        
            guardar_combo(nombre, precio, elementos)

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












        

