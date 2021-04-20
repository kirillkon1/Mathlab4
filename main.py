import numpy as np

from Functions import *
from Utils import *


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


if __name__ == "__main__":

    count = 0
    while True:
        count+=1
        f = open("file2", 'w')

        for i in range(5):
            a1 = np.random.sample() * 10 - 5
            a2 = np.random.sample() * 10 - 5
            f.write(toFixed(a1, 1) + ' ' + toFixed(a1, 1) + '\n')

        f.close()
        PointsArray = readPoint("file2")
        pepe = getPirsonConst(PointsArray)
        if pepe != 1:
            print(f"{pepe} #{count}")
        if abs(pepe) < 0.90:
            print(count)
            print(getPirsonConst(PointsArray))
            break
