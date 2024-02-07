#!/usr/bin/python3
"""This module contains the function save_to_json_file()
   5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Converts a python object to JSON format and write the JSON to a file

        Parameters:
            my_obj : object
            filename (str): filename of the file to store the JSON string

        Return:
            Nothing
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
