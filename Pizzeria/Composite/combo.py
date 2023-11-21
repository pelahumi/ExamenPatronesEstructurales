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
    
    def elementos(self) -> str:
        return ', '.join([child.operation() for child in self._children])
    
    def operation(self) -> int:
        precio = 0
        for child in self._children:
            precio += child.precio
        return precio