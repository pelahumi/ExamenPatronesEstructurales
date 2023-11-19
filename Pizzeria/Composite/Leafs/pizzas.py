from Composite.Leafs.leafs import Leaf

#Creamos la clase pizza

class Pizzas(Leaf):
    """
    Clase que representa a las pizzas
    """

    def operation(self) -> str:
        return "Pizza"