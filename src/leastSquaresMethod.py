import math

from src.Functions.AbstractFunction import AbstractFunction
from src.Functions.LinearFunction import LinearFunction, getPirsonConst
from src.Functions.PolynomialFunction import LinearCrimerMethod, PolynomialFunction
from src.Utils.Point import PointCollection

"""Нахождение функции методотом наименьших квадратов"""


def start(points: PointCollection, fun: AbstractFunction):
    try:
        if fun.getTitle() == 'PolynomialFunction':
            return polynomial_start(points)

        sum_x = 0
        sum_y = 0
        sum_sq_x = 0
        sum_x_y = 0

        for point in points:
            sum_x += point.x
            sum_y += point.y
            sum_sq_x += point.x ** 2
            sum_x_y += point.y * point.x
        if fun.getTitle() != "ExponentialFunction":
            a, b = fun.CrimerMethod(sum_x, sum_y, sum_sq_x, sum_x_y, len(points))
        else:
            b, a = fun.CrimerMethod(sum_x, sum_y, sum_sq_x, sum_x_y, len(points))
        fun.setArg_a(a)
        fun.setArg_b(b)

        e = 0
        s = 0  # measure of deviation

        for point in points:
            e = point.y - fun.find(point.x)
            s += math.pow(e, 2)

        delta = math.sqrt(s / len(points))  # standard deviation

        if delta > 10000000000:
            raise Exception

        return fun, s, delta
    except Exception:
        fun.setArg_a('a')
        fun.setArg_b('b')
        return fun, 'ERR', 'ERR'


"""Нахождение функции методотом наименьших квадратов для полиномиальной функции"""


def polynomial_start(points: PointCollection):
    sum_x = sum_x2 = sum_x3 = sum_x4 = sum_y = sum_x_y = sum_x2_y = 0

    fun = PolynomialFunction()

    for point in points:
        sum_x += point.x
        sum_x2 += point.x ** 2
        sum_x3 += point.x ** 3
        sum_x4 += point.x ** 4
        sum_y += point.y
        sum_x_y += point.x * point.y
        sum_x2_y += point.x ** 2 * point.y

    c, b, a = LinearCrimerMethod(sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_x_y, sum_x2_y, len(points))

    fun.setArg_a(a)
    fun.setArg_b(b)
    fun.setArg_c(c)

    # if getPirsonConst(points) > 0.9:
    #     fun = LinearFunction()
    #     fun.a = b
    #     fun.b = c

    e = 0
    s = 0  # measure of deviation

    for point in points:
        e = point.y - fun.find(point.x)
        s += math.pow(e, 2)

    delta = math.sqrt(s / len(points))  # standard deviation

    return fun, s, delta
