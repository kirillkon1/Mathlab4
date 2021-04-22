import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import get_determinant, toFixed


class PolynomialFunction(AbstractFunction):

    color = "violet"

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
        return f'{toFixed(self.a)}*x^2 + {toFixed(self.b)}x + {toFixed(self.c)}'

    def CrimerMethod(self, sum_x, sum_y, sum_sq_x, sum_x_y, n: int):
        return 0




'''
        ( n       sum_x   sum_x2 | sum_y    )
        ( sum_x   sum_x2  sum_x3 | sum_x_y  )
        ( sum_x2  sum_x3  sum_x4 | sum_x2_y )
'''


def LinearCrimerMethod(sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_x_y, sum_x2_y, n):
    delta = get_determinant(n, sum_x, sum_x2,
                            sum_x, sum_x2, sum_x3,
                            sum_x2, sum_x3, sum_x4)

    delta1 = get_determinant(sum_y, sum_x, sum_x2,
                             sum_x_y, sum_x2, sum_x3,
                             sum_x2_y, sum_x3, sum_x4)

    delta2 = get_determinant(n, sum_y, sum_x2,
                             sum_x, sum_x_y, sum_x3,
                             sum_x2, sum_x2_y, sum_x4)

    delta3 = get_determinant(n, sum_x, sum_y,
                             sum_x, sum_x2, sum_x_y,
                             sum_x2, sum_x3, sum_x2_y)

    return delta1 / delta, delta2 / delta, delta3 / delta
