#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        may = my_list[0]
        for i in my_list:
            if i > may:
                may = i
        return may
    return None
