import numpy as np

from src.Functions.AbstractFunction import AbstractFunction


class PolynomialFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'PolynomialFunction'

    def __init__(self, arg_a: float, arg_b: float, arg_c: float) -> None:
        super().__init__(arg_a, arg_b)
        self.c = arg_c

    def find(self, x: float) -> float:
        return self.a * pow(x, 2) + self.b * x + self.c

    def setArg_c(self, arg_c):
        self.c = arg_c

    def getStringFunction(self) -> str:
        return f'{self.a}*x^2 + {self.b}x + {self.c}'


    def CrimerMethod(sum_x, sum_y, sum_sq_x, sum_x_y, n: int):
        pass

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
