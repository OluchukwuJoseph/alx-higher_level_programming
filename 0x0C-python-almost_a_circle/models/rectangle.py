#!/usr/bin/python3
"""This model contains the Rectangle class
   models/rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """
        A class that inherits Base
        This class has 9 public methods an initialization method, 4 getter
        methods, and 4 setter method.
        It also has 5 private instance variables, which are:
            - width (int)
            - height (int)
            - y (int)
            - x (int)
            - id (int) -> parent class variable
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Intialization method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter method
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
            height getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter method
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
            x getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x setter method
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
            y getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y setter method
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
            returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            prints the instance of Rectangle with the character #
        """
        for newline in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
            prints the instance of Rectangle in our custom way
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
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
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            if len(args) > len(self.__dict__):
                raise ValueError(
                        'Arguments overload, '
                        'Expected atmost 5 arguments'
                        )
            i = 0
            for key in attributes:
                if type(args[i]) is not int:
                    raise TypeError(f"{attributes[i]} must be an integer")
                if ((attributes[i] == 'width' and args[i] <= 0) or
                        (attributes[i] == 'height' and args[i] <= 0)):
                    raise ValueError(f"{attributes[i]} must be > 0")
                if ((attributes[i] == 'x' and args[i] < 0) or
                        (attributes[i] == 'y' and args[i] < 0)):
                    raise ValueError(f"{attributes[i]} must be >= 0")
                if key == 'id':
                    self.__dict__[key] = args[i]
                else:
                    custom_key = '_Rectangle__' + key
                    self.__dict__[custom_key] = args[i]
                i += 1
                if i == len(args):
                    break
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    raise ValueError(f"Unexpected key -> {key}")
                if key == 'id':
                    custom_key = key
                else:
                    custom_key = '_Rectangle__' + key
                if custom_key in self.__dict__:
                    self.__dict__[custom_key] = value

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        custom_dict = {'x': 0, 'y': 0, 'id': 0, 'height': 0, 'width': 0}
        for key, value in self.__dict__.items():
            if key == 'id':
                custom_dict[key] = value
            else:
                custom_key = key[12:]
                custom_dict[custom_key] = value

        return custom_dict
