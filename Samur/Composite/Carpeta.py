from Composite.component import Component
from typing import List

class Carpeta(Component):

    """
    Esta clase representa a los objetos compuestos del arbol
    """

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
    
    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Carpetas: {', '.join(results)}"

        