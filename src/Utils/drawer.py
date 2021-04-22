from src.Functions import AbstractFunction
from src.Utils.Point import PointCollection
import numpy as np
import matplotlib.pyplot as plt

from src.Utils.Utils import getMin_Max_of_points


def drawFunction(points: PointCollection, funcs):


    # print('На графике:\n')
    for fun in funcs:
        min, max = getMin_Max_of_points(points)

        # print(fun.__getattribute__('color'), " -> ", fun.getStringFunction())

        X = np.linspace(min, max, len(points))
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
