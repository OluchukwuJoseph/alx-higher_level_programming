#!/usr/bin/python3
"""This module contains the class Student
   9-student.py
"""


class Student:
    """This class contains 3 private variables and 2 public methods
    """
    def __init__(self, first_name, last_name, age):
        """
            The class constructor.

            Args:
                first_name: the first name of te student
                last_name: the last name of te student
                age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the instance to Json string format
        """
        return self.__dict__
