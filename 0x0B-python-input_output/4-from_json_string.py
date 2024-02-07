#!/usr/bin/python3
"""This module contains the function from_json_string()
   4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """
        Converts json string to python object

        Parameter:
            my_str (str): Json string

        Return:
            Python object represented by Json string
    """
    obj = json.loads(my_str)
    return obj
