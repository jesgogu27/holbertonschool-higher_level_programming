#!/usr/bin/env python3
def no_c(my_string):
    nl = ""
    for i in list(my_string):
        if i != 'c' and i != 'C':
            nl += i
    return nl
