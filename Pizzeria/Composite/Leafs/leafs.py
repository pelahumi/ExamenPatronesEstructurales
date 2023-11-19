from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from Pizzeria.Composite.component import Component

#Creamos la clase abstracta hoja
class Leaf(Component):
    
    def operation(self) -> str:
        return "Hoja"
    

    