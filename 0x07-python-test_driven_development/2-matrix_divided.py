#!/usr/bin/python3


"""
Function that return the divide the elements of a  matrix
"""


def matrix_divided(matrix, div):

    """
    matrix_divide

    Arguments:
        matrix -- main matrix
        div -- divider
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    x = 0
    y = 0
    mat = [x[:] for x in matrix]
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if len(matrix[x]) != len(matrix[y]):
                raise TypeError("Each row of the matrix must" +
                                "have the same size")

            if type(matrix[x][y]) is not int and \
               type(matrix[x][y]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

            mat[x][y] = round(matrix[x][y] / div, 2)
    return mat
