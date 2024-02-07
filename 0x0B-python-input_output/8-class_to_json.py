#!/usr/bin/python3
"""This module contains the function class_to_json()
   8-class_to_json.py
"""


def class_to_json(obj):
    """
        Converts a class type to a json string

        Parameter:
            obj (class): class

        Return:
            Json string representation of class
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
