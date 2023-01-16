#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    points = list_of_integers
    try:
        size = points.__len__()
        if size == 0:
            return None
    except TypeError as e:
        return None
    highs = sorted(points)

    for high in reversed(highs):
        if 0 < points.index(high) < size:
            return high
    if sorted(highs)[0] == list(reversed(sorted(highs)))[0]:
        return sorted(highs)[0]
    return None
