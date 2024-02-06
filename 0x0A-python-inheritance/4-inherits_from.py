#!/usr/bin/python3
"""This module contains the inherits_from() function
   4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """This function check if obj is an instance that has a parent "a_class"
        Parameters:
            obj: object
            a_class: class
        Return:
            True if obj is an instance that has a parent "a_class"
            Otherwise return False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
