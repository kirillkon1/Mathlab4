import math

from src.Functions.AbstractFunction import AbstractFunction


class LogarithmicFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'LogarithmicFunction'

    def find(self, x: float) -> float:
        return self.a * math.log(x) + self.b

    def getStringFunction(self) -> str:
        return f'{self.a}*ln(x) + {self.b}'
