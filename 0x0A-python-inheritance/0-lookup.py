#!/usr/bin/python3
"""0-lookup.py
   This Directory contains the lookup function
"""


def lookup(obj):
    """This function returns all the methods and attributes in obj.

        Parameter:
            obj (class): The class we seek to know its attributes

        Return:
            A list contaning the attributes of obj
    """
    return dir(obj)
