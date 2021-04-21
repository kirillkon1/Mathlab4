from src.Utils.Utils import *
from src.Legacy.SimpleIterationMethod import simpleIteration


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


fileName = "../file2"

if __name__ == "__main__":

    PointsArray = readPoint(fileName)

    if PointsArray.__len__() < 12:
        print("Так не интересно")

    matrix = [[2, 2, 10, 14], [10, 1, 1, 12], [2, 10, 1, 13]]

    # print(matrix[1])


    answer = matrix[0]

    answer = simpleIteration(matrix)

    print(answer)
