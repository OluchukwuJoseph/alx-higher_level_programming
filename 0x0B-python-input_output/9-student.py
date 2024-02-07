#!/usr/bin/python3
"""This module contains the class Student
   9-student.py
"""
import json


class Student:
    """
        This class contains 3 private variables and 2 public methods
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Converts the instance to Json string format
        """
        json_string = json.dumps(self.__dict__)
        obj = json.loads(json_string)
        return obj
