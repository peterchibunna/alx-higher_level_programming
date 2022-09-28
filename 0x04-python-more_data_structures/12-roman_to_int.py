#!/usr/bin/python3
def roman_to_int(ss):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for idx, i in enumerate(ss):
        prev = ss[idx - 1] if idx != 0 else None
        if prev is not None and romans[prev] < romans[i]:
            n -= romans[i]
        else:
            n += romans[i]
    return abs(n)
