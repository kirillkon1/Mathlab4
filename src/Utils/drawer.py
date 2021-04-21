from src.Functions import AbstractFunction
from src.Utils.Point import PointCollection
import numpy as np
import matplotlib.pyplot as plt

from src.Utils.Utils import getMin_Max_of_points


def drawFunction(points: PointCollection, fun: AbstractFunction):

    min, max = getMin_Max_of_points(points)

    X = np.linspace(min - 1, max + 1, len(points)**2)
    Y = fun.find(X)

    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(X, Y)

    if answer != 'null':
        plt.scatter(answer, fun.find(answer), color="red")
        plt.scatter(a, 0, color="green")
        plt.scatter(b, 0, color="green")
    else:
        plt.scatter(a, 0, color="w")
        plt.scatter(b, 0, color="w")

    plt.show()