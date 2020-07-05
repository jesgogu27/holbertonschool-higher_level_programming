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

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")


    mat = [x[:] for x in matrix]
    tam = len(matrix[0])
    for x in range(len(matrix)):
        if type(matrix[x]) is not list or len(matrix[0]) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if tam != len(matrix[x]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(len(matrix[x])):
            if type(mat[x][y]) is not int and \
               type(mat[x][y]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

            mat[x][y] = round(matrix[x][y] / div, 2)
    return mat