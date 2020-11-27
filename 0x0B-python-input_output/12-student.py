#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """clas student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """define to json"""
        if attrs is None:
            return self.__dict__

        my_dict = {}
        for x in attrs:
            if x in self.__dict__:
                my_dict[x] = self.__dict__[x]
        return my_dict
