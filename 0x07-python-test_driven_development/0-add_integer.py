#!/usr/bin/python3
"""
Function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    add_integer: plus two number integer

    Arguments:
        a {int} -- integer one
        b {int} -- integer two

    Raises:
        TypeError: if arguments is not a integer
        TypeError: if argumest  is not a integer

    Returns:
        int -- plus of integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    else:
        if type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")

    x = int(a)
    y = int(b)
    return x + y
