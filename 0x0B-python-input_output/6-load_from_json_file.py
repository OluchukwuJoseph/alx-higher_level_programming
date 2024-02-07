#!/usr/bin/python3
"""This module contains the function load_from_json_file()
   6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
        Convert the contents of a Json file to a python object

        Parameter:
            filename (str): Filename of Json file

        Return:
            Python object
    """
    with open(filename) as file:
        obj = json.load(file)
        return obj
