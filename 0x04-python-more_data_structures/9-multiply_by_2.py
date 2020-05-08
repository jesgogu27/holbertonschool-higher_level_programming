#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = {}
    for key in a_dictionary:
        d = a_dictionary[key] * 2
        nd[key] = d
    return nd
