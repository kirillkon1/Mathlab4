import numpy as np
from src.Utils.Point import Point, PointCollection


def readPoint(fileName: str) -> PointCollection:
    file = open(fileName, 'r')
    pointlist = PointCollection()
    for line in file:
        try:
            points = line.split()
            if len(points) != 2:
                continue
            point: Point = Point(float(points[0]), float(points[1]))
            pointlist.append(point)
        except Exception:
            continue

    return pointlist


def getMin_Max_of_points(points: PointCollection):
    min = max = points[0]
    for point in points:
            if max < point:
                max = point.x
            if min > point:
                min = point.x

    return min, max

