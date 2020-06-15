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
    m = []
    eerror = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    try:
        fila = matrix[1][0]
    except TypeError:
        return (eerror)
    for i in range(len(matrix)):

        tam = len(matrix[i])
        fl = []
        for j in range(tam):
            if type(j) not in [int, float]:
                raise TypeError(eerror)
            item = matrix[i][j]
            r = round(item / div, 2)
            fl.append(r)
        m.append(fl)
    return(m)
