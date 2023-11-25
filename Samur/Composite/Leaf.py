from Component import Component

class Leaf(Component):

    """
    Esta clase representa a los objetos hoja del arbol
    """

    def operation(self) -> str:
        return "Leaf"