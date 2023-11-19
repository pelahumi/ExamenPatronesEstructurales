from Composite.Leafs.leafs import Leaf

class Postres(Leaf):
    """
    Clase que representa a las postres
    """

    def operation(self) -> str:
        return "Postre"

class TartaQueso(Postres):
    """
    Clase que representa a la tarta de queso
    """

    def operation(self) -> str:
        return "Tarta de queso"

class Flan(Postres):
    """
    Clase que representa al flan
    """

    def operation(self) -> str:
        return "Flan"

class Helado(Postres):
    """
    Clase que representa al helado
    """

    def operation(self) -> str:
        return "Helado"