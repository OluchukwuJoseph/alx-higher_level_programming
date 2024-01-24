#!/usr/bin/python3
class Square:
    """defines square based on size"""

    def __init__(self, size=0):
        """initializes square instance
        Args:
            size (int): size of square
        """
        self.check(size)

    def check(self, size):
        """Checks if the size passes certain conditions

        Args:
            size (int): size of square
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size
