from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed


class PolynomialFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'PolynomialFunction'

    def __init__(self) -> None:
        super().__init__()
        self.c = 0

    def find(self, x: float) -> float:
        return self.a * pow(x, 2) + self.b * x + self.c

    def setArg_c(self, arg_c):
        self.c = arg_c

    def getStringFunction(self) -> str:
        return f'{toFixed(self.a, 5)}*x^2 + {toFixed(self.b)}x + {toFixed(self.c)}'

    def CrimerMethod(self, sum_x, sum_y, sum_sq_x, sum_x_y, n: int):
        return 0
