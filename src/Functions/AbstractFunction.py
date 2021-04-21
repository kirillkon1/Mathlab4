from abc import ABC, abstractmethod


class AbstractFunction(ABC):
    def __init__(self, arg_a: float, arg_b: float) -> None:
        super().__init__()
        self.a = arg_a
        self.b = arg_b

    @abstractmethod
    def find(self, x: float) -> float:
        pass

    @abstractmethod
    def getTitle(self) -> str:
        return "AbstractFunction"

    @abstractmethod
    def getStringFunction(self) -> str:
        return 'baobab'

    def setArg_a(self, arg_a):
        self.a = arg_a

    def setArg_b(self, arg_b):
        self.b = arg_b

    def CrimerMethod(self, sum_x, sum_y, sum_sq_x, sum_x_y, n: int):
        delta = sum_sq_x * n - sum_x * sum_x
        delta1 = sum_x_y * n - sum_x * sum_y
        delta2 = sum_sq_x * sum_y - sum_x * sum_x_y

        return delta1 / delta, delta2 / delta
