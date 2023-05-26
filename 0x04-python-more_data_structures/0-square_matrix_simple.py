#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    resl = [[y ** 2 for y in x] for x in matrix]
    return resl
