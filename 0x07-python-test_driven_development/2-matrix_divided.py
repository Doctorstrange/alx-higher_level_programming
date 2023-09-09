#!/usr/bin/python3
# 2-matrix_divided.py
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
       return new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or matrix == []  or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []

    for row in matrix:
        result_row = []

        for element in row:

            div_result = round(element / div, 2)
            result_row.append(div_result)

        result.append(result_row)

    return (result)
