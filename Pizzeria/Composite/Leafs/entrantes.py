from Composite.Leafs.leafs import Leaf

#Creamos la clase pizza

class Entrantes(Leaf):
    """
    Clase que representa a las pizzas
    """

    def operation(self) -> str:
        return "Entrantes"


class Nachos(Entrantes):
    """
    Clase que representa a las pizzas
    """

    def __init__(self) -> None:
        self.precio = 5.00

    def operation(self) -> str:
        return "Nachos"


class Alitas(Entrantes):
    """
    Clase que representa a las pizzas
    """

    def __init__(self) -> None:
        self.precio = 5.00

    def operation(self) -> str:
        return "Alitas"
    
class Aroscebolla(Entrantes):
    """
    Clase que representa a las pizzas
    """

    def __init__(self) -> None:
        self.precio = 5.00

    def operation(self) -> str:
        return "Aros de cebolla"