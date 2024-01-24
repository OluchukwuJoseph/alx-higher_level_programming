#!/usr/bin/python3
class Square:
    """defines square based on size

    Attributes:
        None
    """

    def __init__(self, size=0):
        """initializes square instance
        Args:
            self: the instance being created
            size: size of square
        Return:
            Nothing
        """
        self.check(size)

    def check(self, size):
        """Checks if the size passes certain conditions
        Args:
            self: the instance being created
            size: size of square
        Return:
             Nothing
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size


