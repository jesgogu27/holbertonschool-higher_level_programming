#!/usr/bin/python3
"""Define Rectangle """


class Rectangle:
    """Define Rectangle """
    def __init__(self, width=0, height=0):
        """Instantiation rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @property
    def height(self):
        """retrieve width"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return permriter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print # for user"""
        cad = ""
        if self.__width == 0 or self.__height == 0:
            return cad

        for width in range(self.__height - 1):
            cad = cad + ("#" * self.__width) + '\n'
        cad = cad + ("#" * self.__width)
        return cad

    def __repr__(self):
        """printed repr"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """printed repr"""
        return ("Bye rectangle...")
