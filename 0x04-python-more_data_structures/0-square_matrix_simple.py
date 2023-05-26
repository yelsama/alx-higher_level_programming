#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    resl = [[0 for i in range(3)] for i in range(3)]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            resl[i][j] = matrix[i][j] ** 2
    return resl
