import math

import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Point import Point, PointCollection


def readPoint(fileName: str) -> PointCollection:
    file = open(fileName, 'r')
    pointlist = PointCollection()
    for line in file:
        try:
            points = line.split()
            if len(points) != 2:
                print(f'Пропущена строка {line}')
                continue
            point: Point = Point(float(points[0]), float(points[1]))
            pointlist.append(point)
        except Exception:
            print(f'Пропущена строка {line}')
            continue

    return pointlist


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def getMin_Max_of_points(points: PointCollection):
    min = max = points[0]
    for point in points:
        if max < point:
            max = point.x
        if min > point:
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
