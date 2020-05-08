#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nl = []
    for i in list(matrix):
        nl.append(list(map(lambda i: i ** 2, i)))
    return nl
