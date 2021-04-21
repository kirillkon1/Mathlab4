import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import get_determinant


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
        return f'{self.a}*x^2 + {self.b}x + {self.c}'

    def CrimerMethod(self, sum_x, sum_y, sum_sq_x, sum_x_y, n: int):
        return 0


def __getPirsonConst(points: list):
    mean_x = __meanX(points)
    mean_y = __meanY(points)

    sum1 = 0
    sum2 = 0
    sum3 = 0
    for point in points:
        sum1 += (point.x - mean_x) * (point.y - mean_y)
        sum2 += pow(point.x - mean_x, 2)
        sum3 += pow(point.y - mean_y, 2)

    return sum1 / np.sqrt(sum2 * sum3)


def __meanX(points: list) -> float:
    sum = 0
    for point in points:
        sum += float(point.__getattribute__('x'))  # Just testing

    return sum / len(points)


def __meanY(points: list) -> float:
    sum = 0
    for point in points:
        sum += float(point.__getattribute__('y'))

    return sum / len(points)


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
