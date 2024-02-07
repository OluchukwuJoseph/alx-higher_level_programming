#!/usr/bin/python3
import json
"""This module contains the function from_json_string()
   4-from_json_string.py
"""


def from_json_string(my_str):
    obj = json.loads(my_str)
    return obj
