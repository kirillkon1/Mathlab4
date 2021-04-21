import math

from src.Functions.AbstractFunction import AbstractFunction


class ExponentialFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'ExponentialFunction'

    def find(self, x: float) -> float:
        return self.a * pow(math.e, self.b * x)

    def getStringFunction(self) -> str:
        return f'{self.a}*e^{self.b}x'
