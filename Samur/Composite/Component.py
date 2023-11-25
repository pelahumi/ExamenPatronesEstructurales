from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):

    """
    Esta clase es la interfaz que define el comportamiento de los objetos del arbol
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent
    
    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False
    
    @abstractmethod
    def operation(self) -> str:
        pass