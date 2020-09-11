#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return (set_1.intersection(set_2))

set_1 = [3, 5, 8, 11, 22]
set_2 = [6, 7, 11, 22, 27]

print(only_diff_elements(set_1, set_2))
