#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """A class that has instance attributes and methods"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """Retrieves the private instance attribute height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if (type(value) is not int or value is None):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if (type(value) is not int or value is None):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
