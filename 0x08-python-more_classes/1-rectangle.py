#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """A class that has instance attributes and methods"""
    def __init__(self, width=0, height=0):
        self.width(width)
        self.height(height)

    def width(self):
        """Retrieves the private instance attribute width"""
        return self.width

    def height(self):
        """Retrieves the private instance attribute height"""
        return self.height

    def width(self, value):
        """sets the private instance attribute width

            Parameters:
                self - The instance that called the method
                width(int) - new height value

            Return:
                Nothing
        """
        try:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.width = value
        except Exception as error:
            if isinstance(error, TypeError):
                raise TypeError("width must be an integer")
            else:
                print(f"An unknown error {error} occured")

    def height(self, value):
        """sets the private instance attribute height

            Parameters:
                self - The instance that called the method
                height(int) - new height value

            Return:
                Nothing
        """
        try:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.height = value
        except Exception as error:
            if isinstance(error, TypeError):
                raise TypeError("height must be an integer")
            else:
                print(f"An unknown error {error} occured")
