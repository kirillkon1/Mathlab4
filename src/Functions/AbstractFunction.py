from abc import ABC, abstractmethod


class AbstractFunction(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.a = '-'
        self.b = '-'
        self.c = '-'

    @abstractmethod
    def find(self, x: float) -> float:
        pass

    @abstractmethod
    def getTitle(self) -> str:
        pass

    @abstractmethod
    def getStringFunction(self) -> str:
        return 'baobab'

    def setArg_a(self, arg_a):
        self.a = arg_a

    def setArg_b(self, arg_b):
        self.b = arg_b


    """
       (a     b    |    c  )
       (d     e    |    f  )
    """
def CrimerMethod(a: float, b: float, c: float, d: float, e: float, f: float):
    delta = a * e - b * d
    delta1 = c * e - b * f
    delta2 = a * f - d * c

    return delta1 / delta, delta2 / delta
