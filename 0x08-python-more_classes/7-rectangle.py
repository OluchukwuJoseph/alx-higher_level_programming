#!/usr/bin/python3
"""5-rectangle.py"""


class Rectangle:
    """A class that has instance attributes and methods"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @property
    def height(self):
        """Retrieves height"""
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

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """This method print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return f''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i is not self.__height - 1:
                    print()
            return f''

    def __repr__(self):
        """This method when paired with eval() can create a new instance
        with the same value as the current instance"""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """This method will be executed when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
        return None
