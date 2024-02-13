#!/usr/bin/python3
"""This module contains the class Square
   models/square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This class inherits from the Rectangle.
        The attributes of this class are:
            - id (int)
            - width (int)
            - height (int)
            - x (int)
            - y (int)
            - size (int)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialization method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            prints the instance of Rectangle in our custom way
        """
        return (
                f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}"
        )

    def update(self, *args, **kwargs):
        """
            updates the value of each attribue

            1st argument is the id attribute
            2nd argument is the width attribute
            3rd argument is the height attribute
            4th argument is the x attribute
            5th argument is the y attribute
        """
        attributes = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            if len(args) > len(attributes):
                raise ValueError(f"Argument overload, Expected atmost 4 arguments")
            i = 0
            for i in range(len(args)):
                if type(args[i]) is not int:
                    raise TypeError(f"{attributes[i]} must be an integer")
                if attributes[i] == 'size' and args[i] <= 0:
                    raise ValueError(f"{attributes[i]} must be > 0")
                if ((attributes[i] == 'x' and args[i] < 0) or
                        (attributes[i] == 'y' and args[i] < 0)):
                    raise ValueError(f"{attributes[i]} must be >= 0")
                custom_key = '_Rectangle__' + attributes[i]
                self.__dict__[custom_key] = args[i]
                if attributes[i] == 'size':
                    self.__dict__['_Rectangle__height'] = args[i]
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    raise ValueError(f"Unexpected key -> {key}")
                if key == 'id':
                    custom_key = key
                else:
                    custom_key = '_Rectangle__' + key
                    if custom_key == '_Rectangle__size':
                        self.__dict__['_Rectangle__width'] = value
                        self.__dict__['_Rectangle__height'] = value
                    else:
                        self.__dict__[custom_key] = value
