from Composite.component import Component
from typing import List

#Creamos la clase combo
class Combo(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def añadir_componente(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        precio = 0
        for child in self._children:
            precio += child.precio
        return f"El precio del combo es: {precio} euros. Y contiene: {', '.join([child.operation() for child in self._children])}"