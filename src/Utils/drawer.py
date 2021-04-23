from src.Utils.Point import PointCollection
import numpy as np
import matplotlib.pyplot as plt

from src.Utils.Utils import getMin_Max_of_points


def drawFunction(points: PointCollection, funcs):
    for fun in funcs:
        min, max = getMin_Max_of_points(points)

        X = np.linspace(min - 1, max + 1, len(points) ** 2)
        Y = fun.find(X)

        ax = plt.gca()
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.plot(X, Y)

    for point in points:
        plt.scatter(point.x, point.y, color="black")

    plt.show()
