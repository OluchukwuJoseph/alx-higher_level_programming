#!/usr/bin/python3
import json
"""This module contains the to_json_string() function
   3-to_json_string.py
"""


def to_json_string(my_obj):
    """
        Serializes a python object to a JSON string

        Parameter:
            my_obj: python object

        Return:
            JSON format of my_obj
    """
    json_string = json.dumps(my_obj)
    return json_string
