#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
