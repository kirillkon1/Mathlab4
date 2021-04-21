def simpleIteration(matrix):
    matrix = __refactorMatrix(matrix)
    epsilon = 0.00001
    rang = len(matrix)
    equally = []
    result = []
    Xn = []

    for i in range(0, rang):
        equally.append(matrix[i][rang])
        result.append(equally[i] / matrix[i][i])

    while True:
        max = 0

        for i in range(0, rang):
            Xn.append(equally[i] / matrix[i][i])

            for j in range(0, rang):
                if i != j:
                    Xn[i] = Xn[i] - matrix[i][j] / matrix[i][i] * result[j]

        for i in range(0, rang):
            if abs(result[i] - Xn[i]) > max:
                max = abs(result[i] - Xn[i])
            result[i] = Xn[i]

        if max < epsilon:
            break

    return result


def __refactorMatrix(matrix):
    new_matrix = matrix
    tmpmatrix = matrix
    print(tmpmatrix)
    rang = len(tmpmatrix)
    queue = []
    for i in range(0, rang):
        queue.append(__maxElementPosition(tmpmatrix[i]))

        for j in range(0, i):
            if queue[j] == queue[i]:
                print("wrong matrix -> SimpleIterationMethod")  # breakpoints suck
                # return new_matrix

    return __stupidpython(matrix, queue)


def __maxElementPosition(line: list):
    queue = -1
    for i in range(0, len(line) - 1):
        max = 0
        for j in range(0, len(line) - 1):
            if i != j:
                max += abs(line[j])

            if line[i] > max:
                queue = i
                break
    return queue


def __stupidpython(matrix, queue) -> list:
    new_matrix = []
    tmp = 0
    tmp1 = 0
    while True:
        if queue[tmp % len(queue)] == tmp1:
            new_matrix.append(matrix[tmp % len(queue)])
            tmp1 += 1
            if tmp1 == len(queue):
                break

        tmp += 1

    return new_matrix
