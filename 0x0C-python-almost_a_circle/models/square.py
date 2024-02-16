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

    @property
    def size(self):
        """
            Size getter method
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size setter method
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

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
            2nd argument is the size attribute
            3th argument is the x attribute
            4th argument is the y attribute
        """
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            if len(args) > len(attributes):
                raise ValueError(
                    'Argument overload, '
                    'Expected atmost 4 arguments'
                )
            i = 0
            for i in range(len(args)):
                # validate argument value
                if type(args[i]) is not int:
                    raise TypeError(f"{attributes[i]} must be an integer")
                if attributes[i] == 'size' and args[i] <= 0:
                    raise ValueError(f"{attributes[i]} must be > 0")
                if ((attributes[i] == 'x' and args[i] < 0) or
                        (attributes[i] == 'y' and args[i] < 0)):
                    raise ValueError(f"{attributes[i]} must be >= 0")
                # update value
                if attributes[i] == 'id':
                    self.__dict__['id'] = args[i]
                elif attributes[i] == 'size':
                    self.__dict__['_Rectangle__width'] = args[i]
                    self.__dict__['_Rectangle__height'] = args[i]
                else:
                    custom_key = '_Rectangle__' + attributes[i]
                    self.__dict__[custom_key] = args[i]
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    raise ValueError(f"Unexpected key -> {key}")
                if key == 'id':
                    self.__dict__[key] = value
                else:
                    custom_key = '_Rectangle__' + key
                    if custom_key == '_Rectangle__size':
                        self.__dict__['_Rectangle__width'] = value
                        self.__dict__['_Rectangle__height'] = value
                    else:
                        self.__dict__[custom_key] = value

    def to_dictionary(self):
        """
             returns the dictionary representation of a Square Instance
        """
        custom_dict = {'id': 0, 'x': 0, 'size': 0, 'y': 0}
        for key, value in self.__dict__.items():
            if key == 'id':
                custom_dict[key] = value
            else:
                custom_key = key[12:]
                if custom_key == 'width' or custom_key == 'height':
                    custom_dict['size'] = value
                else:
                    custom_dict[custom_key] = value
        return custom_dict
