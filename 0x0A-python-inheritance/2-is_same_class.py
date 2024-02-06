#!/usr/bin/python
"""This module contains is_same_class() function
   2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """This function checks if obj is a instance of a_class
        Parameters:
            obj: instance
            a_class: class
        Return:
            True if object is an instance of a_class
            Otherwise return false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
