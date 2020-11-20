#!/usr/bin/python3
"""
   Class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass"""

    def __init__(self, width, height):
        """
        __init__ - initializator
        width - width rectangle
        height - height rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """ The area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        '''Return the string representation of a rectangle'''
        msg = '[Rectangle] {}/{}'.format(self.__width, self.__height)
        return msg
