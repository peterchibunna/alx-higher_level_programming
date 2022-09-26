#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_l = []
    for i in my_list:
        new_l.append(i % 2 == 0)
    return new_l
