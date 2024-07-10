#!/usr/bin/python3
"""This module contains the find_peak function"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while (high > low):
        mid = (high + low) // 2

        if (list_of_integers[mid] < list_of_integers[mid + 1]):
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
