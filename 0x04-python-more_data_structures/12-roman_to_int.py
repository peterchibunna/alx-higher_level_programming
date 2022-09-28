#!/usr/bin/python3
def roman_to_int(ss):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    for index, char in enumerate(ss):
        current_num = romans[char]
        last_num = romans[ss[index - 1]]

        if index != 0 and last_num < current_num:
            sum += current_num - 2 * last_num
        else:
            sum += current_num
    return sum
