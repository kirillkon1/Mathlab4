import math

from src.Functions.AbstractFunction import AbstractFunction, CrimerMethod
from src.Functions.LinearFunction import LinearFunction, getPirsonConst
from src.Functions.PolynomialFunction import LinearCrimerMethod, PolynomialFunction
from src.Utils.Point import PointCollection

"""Нахождение аппроксимирующей функции методотом наименьших квадратов"""


def start(points: PointCollection, fun: AbstractFunction):
    try:

        if fun.getTitle() == 'PolynomialFunction':
            return polynomial_start(points)
        elif fun.getTitle() == 'LinearFunction':
            a, b = __linear_approximation(points)
        elif fun.getTitle() == 'LogarithmicFunction':
            a, b = __logarithmic_approximation(points)
        elif fun.getTitle() == 'PowerFunction':
            a, b = __power_approximation(points)
        elif fun.getTitle() == 'ExponentialFunction':
            a, b = __exponential_approximation(points)
        else:
            raise Exception

        fun.setArg_a(a)
        fun.setArg_b(b)

        e = 0
        s = 0  # measure of deviation

        for point in points:
            e = point.y - fun.find(point.x)
            s += math.pow(e, 2)

        delta = math.sqrt(s / len(points))  # standard deviation

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

    e = 0
    s = 0  # measure of deviation

    for point in points:
        e = point.y - fun.find(point.x)
        s += math.pow(e, 2)

    delta = math.sqrt(s / len(points))  # standard deviation

    return fun, s, delta


def __linear_approximation(points: PointCollection):
    sum_x = sum_y = sum_sq_x = sum_x_y = 0

    for point in points:
        sum_x += point.x
        sum_y += point.y
        sum_sq_x += point.x ** 2
        sum_x_y += point.y * point.x

    a, b = CrimerMethod(sum_sq_x, sum_x, sum_x_y, sum_x, len(points), sum_y)  # Формулу взял из лекции
    return a, b


def __logarithmic_approximation(points: PointCollection):
    sum_lnx = sum_lnx2 = sum_y = sum_lnx_y = 0

    for point in points:
        sum_lnx += math.log(point.x)
        sum_lnx2 += pow(math.log(point.x), 2)
        sum_y += point.y
        sum_lnx_y += point.y * math.log(point.x)

    b, a = CrimerMethod(len(points), sum_lnx, sum_y, sum_lnx, sum_lnx2, sum_lnx_y)  # a + b * ln(x)
    return a, b


def __exponential_approximation(points: PointCollection):
    sum_x = sum_x2 = sum_lny = sum_x_lny = 0

    for point in points:
        sum_x += point.x
        sum_x2 += pow(point.x, 2)
        sum_lny += math.log(point.y)
        sum_x_lny += math.log(point.y) * point.x

    a, b = CrimerMethod(len(points), sum_x, sum_lny, sum_x, sum_x2, sum_x_lny)
    a = pow(math.e, a)
    return a, b


def __power_approximation(points: PointCollection):
    sum_lnx = sum_lny = sum_lnx2 = sum_lnx_lny = 0
    n = len(points)

    for point in points:
        sum_lnx += math.log(point.x)
        sum_lny += math.log(point.y)
        sum_lnx2 += math.log(point.x) ** 2
        sum_lnx_lny += math.log(point.x) * math.log(point.y)

    a, b = CrimerMethod(n, sum_lnx, sum_lny, sum_lnx, sum_lnx2, sum_lnx_lny)
    a = pow(math.e, a)
    return a, b
