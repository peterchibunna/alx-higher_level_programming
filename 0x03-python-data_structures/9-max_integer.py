#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return None
    h = reversed(my_list.sort())[0]
    return h
