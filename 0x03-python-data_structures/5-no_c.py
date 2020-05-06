#!/usr/bin/env python3
def no_c(my_string):
    nl = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            nl = nl + i
    return nl
