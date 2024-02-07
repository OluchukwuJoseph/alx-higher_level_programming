#!/usr/bin/python3
"""This module contains the class Student
   11-student.py
"""


class Student:
    """This class contains 3 private variables and 3 public method"""
    def __init__(self, first_name, last_name, age):
        """
            The class constructor.

            Args:
                first_name: the first name of te student
                last_name: the last name of the student
                age: the age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the instance to Json string format
        """
        obj = self.__dict__
        if attrs is None:
            return obj
        else:
            new_obj = {}
            for key in attrs:
                if key in obj:
                    new_obj.update({key: obj[key]})
            return new_obj

    def reload_from_json(self, json):
        """Replaces insatnce variable names and values to json (dictionary)
           names and values
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
