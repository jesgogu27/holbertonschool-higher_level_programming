#!/usr/bin/python3

"""
   Class BaseGeometry
"""


class BaseGeometry:

    """
        BaseGeometry
    """

    def area(self):
        """
        area - return a msj Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - validate a number
        name - a string
        value - value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
