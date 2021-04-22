import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed


class LinearFunction(AbstractFunction):

    color = "darkorange"

    def __init__(self) -> None:
        super().__init__()

    def getTitle(self) -> str:
        return 'LinearFunction'

    def find(self, x: float) -> float:
        return self.a * x + self.b

    def getStringFunction(self) -> str:
        return f'{toFixed(self.a)}*x^{toFixed(self.b)}'


def getPirsonConst(points: list):
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
