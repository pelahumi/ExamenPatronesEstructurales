from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

#Creamos la clase abstracta componente
class Component(ABC):
    """
    La clase Component declara la interfaz común para objetos en una composición,
    """

    @property
    def parent(self) -> Component:
        return self._parent
    
    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def añadir_componente(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass   

