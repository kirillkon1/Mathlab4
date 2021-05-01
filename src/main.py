from src.Functions.ExponentialFunction import ExponentialFunction
from src.Functions.LinearFunction import LinearFunction, getPirsonConst
from src.Functions.LogarithmicFunction import LogarithmicFunction
from src.Functions.PolynomialFunction import PolynomialFunction
from src.Functions.PowerFunction import PowerFunction
from src.Utils.Answer import Answer
from src.Utils.Utils import *
from src.Utils.drawer import drawFunction
from src.leastSquaresMethod import start

fileName = "../file1"

if __name__ == "__main__":

    # ------------Заполнение массива точками----------------
    points_list = readPoint(fileName)
    # points_list = userReader()
    # ------------------------------------------------------

    # -----Инициализация всем аппроксимирующих методов-----
    exponential = ExponentialFunction()
    linear = LinearFunction()
    logarithmic = LogarithmicFunction()
    power = PowerFunction()
    polynomial = PolynomialFunction()
    functions = [exponential, linear, logarithmic, power, polynomial]
    # -----------------------------------------------------

    answer = []
    min_deviation = 100000  # минимальное отклонение

    funcs = []

    # -----Вывод ответа-------
    for tmp_fun in functions:

        # fun - функция, measure_of_deviation - мера отклонения, standard_deviation - cреднеквадратичное отклонение
        fun, measure_of_deviation, standard_deviation = start(points_list, tmp_fun)

        if measure_of_deviation == 'ERR':
            continue
        else:
            answer.append(Answer(fun, measure_of_deviation, standard_deviation))  # Записываю ответ
        if standard_deviation < 200:
            funcs.append(fun)

        if min_deviation > standard_deviation:
            min_deviation = standard_deviation
            necessary_function: AbstractFunction = fun

    # --Вывод ответов в консоль--
    for one_answer in answer:
        print(one_answer)

    print(f'\nНаиболее подходящая функция: {necessary_function.getTitle()} : ', necessary_function.getStringFunction())
    print(f"со средним квадратичным отклонением {toFixed(standard_deviation)}")
    if necessary_function.getTitle() == 'LinearFunction':
        print(f"Коэффициент корреляции = {getPirsonConst(points_list)}")

    # -----Отрисовка графиков-------
    print("На графике функции: ", end='')
    for i in funcs:
        print(i.getTitle(), end=' ')
    print()
    drawFunction(points_list, funcs)
    funcs.clear()
    funcs.append(necessary_function)
    drawFunction(points_list, funcs)
