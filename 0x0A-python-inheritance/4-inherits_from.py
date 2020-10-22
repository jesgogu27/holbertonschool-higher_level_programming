#!/usr/bin/python3

"""
 is true o false
"""


def inherits_from(obj, a_class):

    """
    inherits_from - return true o false
    obj - object
    a_class - class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
