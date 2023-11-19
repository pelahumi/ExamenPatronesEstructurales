from Composite.Leafs.leafs import Leaf

class Bebidas(Leaf):
    """
    Clase que representa a las bebidas
    """

    def operation(self) -> str:
        return "Bebida"
    
class Agua(Bebidas):
    """
    Clase que representa al agua
    """

    def operation(self) -> str:
        return "Agua"

class Refresco(Bebidas):
    """
    Clase que representa al refresco
    """

    def operation(self) -> str:
        return "Refresco"

class Cerveza(Bebidas):
    """
    Clase que representa a la cerveza
    """

    def operation(self) -> str:
        return "Cerveza"
