#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = [row[:] for row in matrix]
    index = 0
    for row in matrix:
        count = 0
        for column in row:
            matrix_copy[index][count] = column**2
            count += 1
        index += 1
    return (matrix_copy)
