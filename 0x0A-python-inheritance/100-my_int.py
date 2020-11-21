#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, anyy):
        return super().__ne__(anyy)

    def __ne__(self, anyy):
        return super().__eq__(anyy)
