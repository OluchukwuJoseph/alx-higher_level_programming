#!/usr/bin/python3
"""This module contains the is_kind_of_class() function
   3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """checks if the type of the object is kind of the same as a_class
        Parameters:
            obj: object
            a_class: Class
        Return:
            True if the object is kind of the same as a_class
            otherwise return false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
