#!/usr/bin/python3
"""This module contains a class BaseGeometry
   6-base_geometry.py
"""


class BaseGeometry:
    """This class has two public method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the input given to name and value

            Return:
                Nothing
        """
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.value = value
