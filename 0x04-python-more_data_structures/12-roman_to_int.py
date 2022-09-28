#!/usr/bin/python3
def roman_to_int(ss):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    ss = ss.replace("IV", "IIII")
    ss = ss.replace("IX", "VIIII")
    ss = ss.replace("XL", "XXXX")
    ss = ss.replace("XC", "LXXXX")
    ss = ss.replace("CD", "CCCC")
    ss = ss.replace("CM", "DCCCC")
    # replace those ambiguous ones that go backward and forward to always forward
    # ie. the forwards only
    for idx, i in enumerate(ss):
        total += romans[i]
    return abs(total)
