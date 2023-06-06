#!/usr/bin/python3

def matrix_divided(matrix, div):
    """check the code to understand"""
    _len = len(matrix[0])
    new_mat = [[0 for i in range(_len)] for i in range(len(matrix))]
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[i]) != _len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")
            new_mat[i][j] = round(matrix[i][j] / div, 2)
    return new_mat
