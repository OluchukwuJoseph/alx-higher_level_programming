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
