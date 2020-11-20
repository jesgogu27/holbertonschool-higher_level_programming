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
        self.integer_validator(width, height)
        self.integer_validator(height, height)
        self.__width = width
        self.__height = height
