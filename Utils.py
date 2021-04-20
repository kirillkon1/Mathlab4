import numpy as np
from Point import Point


def readPoint(fileName: str):
    file = open(fileName, 'r')
    pointlist = []
    for line in file:
        try:
            points = line.split()
            if len(points) != 2:
                continue
            point = Point(float(points[0]), float(points[1]))
            pointlist.append(point)
        except Exception:
            continue

    return pointlist


def getPirsonConst(points: list):
    meanX = __meanX(points)
    meanY = __meanY(points)

    sum1 = 0
    sum2 = 0
    sum3 = 0
    for point in points:
        sum1 += (point.x - meanX)*(point.y - meanY)
        sum2 += pow(point.x - meanX, 2)
        sum3 += pow(point.y - meanY, 2)

    return sum1/np.sqrt(sum2*sum3)


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
