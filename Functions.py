import math
from abc import ABC, abstractmethod


class AbstractFunction(ABC):
    def __init__(self, arg_a: float, arg_b: float) -> None:
        super().__init__()
        self.a = arg_a
        self.b = arg_b

    @abstractmethod
    def find(self, x: float) -> float:
        pass

    def setArg_a(self, arg_a):
        self.a = arg_a

    def setArg_b(self, arg_b):
        self.b = arg_b


class LinearFunction(AbstractFunction):

    def find(self, x: float) -> float:
        return self.a * x + self.b


class PolynomialFunction(AbstractFunction):

    def __init__(self, arg_a: float, arg_b: float, arg_c: float) -> None:
        super().__init__(arg_a, arg_b)
        self.c = arg_c

    def find(self, x: float) -> float:
        return self.a * pow(x, 2) + self.b * x + self.c

    def setArg_c(self, arg_c):
        self.c = arg_c


class ExponentialFunction(AbstractFunction):

    def find(self, x: float) -> float:
        return self.a * pow(math.e, self.b * x)


class LogarithmicFunction(AbstractFunction):

    def find(self, x: float) -> float:
        return self.a * math.log(x) + self.b


class PowerFunction(AbstractFunction):

    def find(self, x: float) -> float:
        return self.a * pow(x, self.b)
