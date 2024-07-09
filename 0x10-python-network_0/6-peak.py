#!/usr/bin/python3
"""This module contains the find_peak function"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    peak = 0
    low = 0
    high = len(list_of_integers) - 1

    while ((high + 1) > low):
        if list_of_integers[low] > list_of_integers[high]:
            if list_of_integers[low] > peak:
                peak = list_of_integers[low]
        else:
            if list_of_integers[high] > peak:
                peak = list_of_integers[high]

        high = high - 1
        low = low + 1

    return peak
