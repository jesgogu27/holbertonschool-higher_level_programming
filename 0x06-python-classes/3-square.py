#!/usr/bin/python3
"""Class Square Define a square"""


class Square():
    """Class Square"""
    def __init__(self, size=0):
        """Instantiation Keyword Arguments:
            size {int} -- size of the square (default: {0})
        Raises:
            TypeError: Raises error if type of var size in not int
            ValueError: Raises error if value if is out of range
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a sqaure
        Returns:
            int -- area of square
        """
        res = self.__size**2
        return res
