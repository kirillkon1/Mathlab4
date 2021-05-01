from abc import ABC, abstractmethod


class AbstractFunction(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.a = '-'
        self.b = '-'
        self.c = '-'

    @abstractmethod
    def find(self, x: float) -> float:
        pass

    @abstractmethod
    def getTitle(self) -> str:
        pass

    @abstractmethod
    def getStringFunction(self) -> str:
        return 'baobab'

    def setArg_a(self, arg_a):
        self.a = arg_a

    def setArg_b(self, arg_b):
        self.b = arg_b

    """
       (a     b    |    c  )
       (d     e    |    f  )
    """


def find_by_Crimer_method(a: float, b: float, c: float, d: float, e: float, f: float):
    delta = a * e - b * d
    delta1 = c * e - b * f
    delta2 = a * f - d * c

    return delta1 / delta, delta2 / delta


'''     
Решатель системы методом Крамера
        ( n       sum_x   sum_x2 | sum_y    )
        ( sum_x   sum_x2  sum_x3 | sum_x_y  )
        ( sum_x2  sum_x3  sum_x4 | sum_x2_y )
'''


def find_Crimer_method_by_third_matrix(sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_x_y, sum_x2_y, n):
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


'''
    метод для нахождение детерминанта 

    | a  b  c |
    | d  e  f | = -i * b * d + b * f * g + c * d * h - a * f * h + i * a * e - c * g * e
    | g  h  i |
'''


def get_determinant(a, b, c, d, e, f, g, h, i):
    return -i * b * d + b * f * g + c * d * h - a * f * h + i * a * e - c * g * e
