import math

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Point import PointCollection


def start(points: PointCollection, fun: AbstractFunction):

    if fun.getTitle() == 'PolynomialFunction':
        return polynomial_start(points, fun)

    sum_x = 0
    sum_y = 0
    sum_sq_x = 0
    sum_x_y = 0

    for point in points:
        sum_x += point.x
        sum_y += point.y
        sum_sq_x += point.x ** 2
        sum_x_y += point.y * point.x

    a, b = fun.CrimerMethod(sum_x, sum_y, sum_sq_x, sum_x_y, len(points))
    fun.setArg_a(a)
    fun.setArg_b(b)

    e = 0
    sum = 0

    for point in points:
        e = point.y - fun.find(point.x)
        sum += math.pow(e, 2)

    s = sum
    deviation = math.sqrt(sum / len(points))

    return fun, s, deviation, '-'

def polynomial_start(points: PointCollection, fun: AbstractFunction):
    pass