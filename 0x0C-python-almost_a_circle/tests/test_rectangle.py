#!/usr/bin/python3
"""This module contains test cases for the rectangle class
   tests/test_rectangle.py
"""
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
        This class contains test cases for Rectangle
    """
    def test_task1(self):
        """
            Test if Rectangle actually creates an instance
        """
        r1 = Rectangle(3, 2, 2, 2)
        self.assertIsInstance(r1, Rectangle)
