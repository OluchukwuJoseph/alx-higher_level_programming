#!/usr/bin/python3
"""Module 0-add_integer.py -- A contains a function that adds 2 integers

Functions:
    def add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """This function adds 2 integers
        a (int) - First Integer
        b (int) - Second Integer"""
    try:
        a = int(a)
    except TypeError:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except TypeError:
        raise TypeError("b must be an integer")

    return a + b
