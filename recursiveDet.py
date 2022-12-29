from copy import deepcopy

def smallerMatrix(originalMatrix, row, col):
    newMatrix = deepcopy(originalMatrix)
    newMatrix.remove(originalMatrix[row])
    for i in range(len(newMatrix)):
        newMatrix[i].remove(newMatrix[i][col])
    return newMatrix


def recursiveDet(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            raise Exception("Input must be a square matrix")

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    ans = 0
    for i in range(len(matrix)):
        cofactor = matrix[0][i] * (-1)**i * recursiveDet(smallerMatrix(matrix, 0, i))
        ans += cofactor
    return ans

print(recursiveDet([[1, 0, 0], [0, 5, 0], [0, 0, 1]]))

