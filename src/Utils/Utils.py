import math
import sys

import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Point import Point, PointCollection


def readPoint(file_name: str) -> PointCollection:
    file = open(file_name, 'r')
    pointlist = PointCollection()
    for line in file:
        try:
            points = line.split()
            if len(points) != 2:
                continue
            if points[0] == "0":
                continue
            point: Point = Point(float(points[0]), float(points[1]))
            pointlist.append(point)
        except Exception:

            continue

    # __less_twelve_points(pointlist)
    return pointlist


def toFixed(numObj, digits=2):
    try:
        return f"{numObj:.{digits}f}"
    except Exception:
        return numObj


def getMin_Max_of_points(points: PointCollection):
    point = points[0]
    min = max = point.x
    for point in points:
        if max < point.x:
            max = point.x
        if min > point.x:
            min = point.x

    return min, max


'''
    метод для нахождение детерминанта 
    
    | a  b  c |
    | d  e  f | = -i * b * d + b * f * g + c * d * h - a * f * h + i * a * e - c * g * e
    | g  h  i |
'''


def get_determinant(a, b, c, d, e, f, g, h, i):
    return -i * b * d + b * f * g + c * d * h - a * f * h + i * a * e - c * g * e


'''Чем ближе значение 𝑅^2 к единице (𝑅^2 → 1), тем надежнее
функция 𝜑 аппроксимирует исследуемый процесс.'''


def approximation_reliability(points: PointCollection, fun: AbstractFunction):
    sum_phi = sum_sqr_phi = sum_y_phi = 0
    for point in points:
        sum_phi += fun.find(point.x)
        sum_sqr_phi += fun.find(point.x) * fun.find(point.x)
        sum_y_phi = pow(point.y - fun.find(point.x), 2)
    return 1 - sum_y_phi / (sum_sqr_phi - pow(sum_phi, 2) / len(points))


def userReader() -> PointCollection:
    print("Каким способом желаете ввести данные: файл(1)/клавиатура(2)")
    while True:
        try:
            tmp = int(input())
            if tmp == 1 or tmp == 2:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")
    if tmp == 1:
        global file_name
        while True:
            try:
                print("Введите название файла")
                file_name = input()
                points = readPoint(file_name)
                break
            except FileNotFoundError:
                print("Файл не найден. Повторить попытку? (да\нет)")
                tmp = input()
                if tmp == "нет":
                    print("Завершение работы...")
                    sys.exit(-1)
        return readPoint(file_name)
    else:
        print("Введите желаемое кол-во точек (не меньше 12)")
        while True:
            tmp = 0
            try:
                tmp = int(input())
                if tmp >= 12:
                    break
                print("не меньше 12 точек")
            except Exception:
                print("Неверный ввод")
        print("Введите два числа через пробел (Координаты (X; Y))")
        count = 0
        points: PointCollection = []
        while count < tmp:
            try:
                tmp1 = input().split()
                x, y = float(tmp1[0]), float(tmp1[1])
                points.append(Point(x, y))
                count += 1
            except Exception:
                print("Неверный ввод")
                continue
        print("Готово")
        return points


def __less_twelve_points(points: PointCollection) -> None:
    if len(points) < 12:
        print("Точек меньше 12. Продолжить? (да/нет)")
        while True:
            tmp = input()
            if tmp == "нет":
                print("Завершение работы...")
                sys.exit(-1)
            elif tmp == "да":
                break
