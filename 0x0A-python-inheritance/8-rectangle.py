#!/usr/bin/python3
"""This module contains a class Rectangle
   8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """This class inherits BaseGeometry
       and it has 1 public method and 2 private instance variable
    """
    def __init__(self, width, height):
        """Initializes width and height"""
        self.integer_validator('width', width)
        self.__width = self.value
        self.integer_validator('height', height)
        self.__height = self.value
        del self.name
        del self.value
