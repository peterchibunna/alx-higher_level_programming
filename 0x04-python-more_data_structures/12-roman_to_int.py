#!/usr/bin/python3
def roman_to_int(ss):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0
    for letter in ss:
        value = romans[letter]
        total += value
        if value > prev_value:
            total -= 2 * prev_value
            prev_value = value
    return total
