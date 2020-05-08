#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list.copy()
    for i, f in enumerate(nl):
        if f == search:
            nl[i] = replace
    return nl
