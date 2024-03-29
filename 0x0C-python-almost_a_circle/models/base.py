#!/usr/bin/python3
"""This module contains the Base class
   models/base.py
"""


class Base:
    """
        This class has one method, one class private variable and
        one instance public variable.
        They names and types of these variables are:
            - __nb_objects (int) -> class private variable
            - id (int) -> instance public variable
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialization method
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
             returns the JSON string representation of list_dictionaries
        """
        if type(list_dictionaries) is None:
            return "[]"
        else:
            return str(list_dictionaries)
