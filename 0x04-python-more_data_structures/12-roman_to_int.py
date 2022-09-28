#!/usr/bin/python3
def roman_to_int(ss):
    romans = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_of_num = [romans[char] for char in ss]
    list_of_num = [list_of_num[index] - 2 * list_of_num[index - 1]
                   if list_of_num[index - 1] < list_of_num[index] and index != 0
                   else list_of_num[index]
                   for index in range(len(list_of_num))]
    return sum(list_of_num)
