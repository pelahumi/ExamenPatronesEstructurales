from Composite.Leaf import Leaf

class Documentos(Leaf):

    def __init__(self, nombre, tipo, tamano) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = tamano

    def operation(self) -> str:
        return f"Documento: {self.nombre} - Tipo: {self.tipo} - Tamaño: {self.tamano} MB"
    
