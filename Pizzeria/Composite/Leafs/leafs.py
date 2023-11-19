from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from Composite.component import Component

#Creamos la clase abstracta hoja
class Leaf(Component):

    def __init__(self, precio: float) -> None:
        self.precio = precio
    
    def operation(self) -> str:
        return "Hoja"
    

    