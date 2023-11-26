from Leaf import Leaf

class Links(Leaf):

    def __init__(self, name: str):
        self.name = name

    def operation(self) -> str:
        return self.name