#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in list(matrix):
            print(" ".join("{:d}".format(y)for y in i))
