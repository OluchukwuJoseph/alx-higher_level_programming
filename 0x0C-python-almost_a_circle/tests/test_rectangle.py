#!/usr/bin/python3
"""This module contains test cases for the rectangle class
   tests/test_rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        This class contains test cases for Rectangle
    """
    def test_instance(self):
        """
            Test if Rectangle actually creates an instance
        """
        r1 = Rectangle(3, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(3, 2, 1, 1)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r2.id, 8)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)

    def test_width(self):
        """
            Test the width argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle('2', 3)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r3 = Rectangle(-2, 3)
        with self.assertRaises(TypeError):
            r4 = Rectangle(None, 3)
        with self.assertRaises(TypeError):
            r5 = Rectangle(2.8, 3)
        with self.assertRaises(TypeError):
            r6 = Rectangle([1, 2], 3)
        with self.assertRaises(TypeError):
            r7 = Rectangle({'value': 2}, 3)
        with self.assertRaises(TypeError):
            r8 = Rectangle((1, 2), 3)
        r9 = Rectangle(125400000000000000000000, 3)
        self.assertEqual(r9.width, 125400000000000000000000)

    def test_height(self):
        """
            Test the height argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, '3')
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, None)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3.8)
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, [1, 3])
        with self.assertRaises(TypeError):                                                      
            r5 = Rectangle(2, {'value': 3})
        with self.assertRaises(TypeError):                                                      
            r6 = Rectangle(2, (1, 3))
        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            r8 = Rectangle(2, -3)
        r9 = Rectangle(2, 125400000000000000000000)
        self.assertEqual(r9.height, 125400000000000000000000)

    def test_width_and_height(self):
        """
            Test width and height arguments
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle('2', '3')
        with self.assertRaises(TypeError):
            r2 = Rectangle(None, None)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2.8, 3.8)
        with self.assertRaises(TypeError):
            r4 = Rectangle([1, 2], [1, 3])
        with self.assertRaises(TypeError):
            r5 = Rectangle({'value': 2}, {'value': 3})
        with self.assertRaises(TypeError):
            r6 = Rectangle((1, 2), (1, 3))
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            r8 = Rectangle(-2, -3)
        r9 = Rectangle(234572815350000000000000, 125400000000000000000000)
        self.assertEqual(r9.height, 125400000000000000000000)
        self.assertEqual(r9.width, 234572815350000000000000)

    def test_x(self):
        """
            Test x argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, '2')
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 3, None)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 2.8)
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, 3, [1, 2])
        with self.assertRaises(TypeError):
            r5 = Rectangle(2, 3, {'value': 2})
        with self.assertRaises(TypeError):
            r6 = Rectangle(2, 3, (1, 2))
        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 3, -2)
        r8 = Rectangle(2, 3, 0)
        self.assertEqual(r8.x, 0)
        r9 = Rectangle(2, 3, 125400000000000000000000)
        self.assertEqual(r9.x, 125400000000000000000000)

    def test_y(self):
        """
            Test y argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, '3')
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 3, 2, None)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 2, 3.8)
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, 3, 2, [1, 3])
        with self.assertRaises(TypeError):
            r5 = Rectangle(2, 3, 2, {'value': 3})
        with self.assertRaises(TypeError):
            r6 = Rectangle(2, 3, 2, (1, 3))
        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 3, 2, -3)
        r8 = Rectangle(2, 3, 2, 0)
        self.assertEqual(r8.y, 0)
        r9 = Rectangle(2, 3, 2, 125400000000000000000000)
        self.assertEqual(r9.y, 125400000000000000000000)

    def test_x_and_y(self):
        """
            Test width and height arguments
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, '2', '3')
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 3, None, None)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 2.8, 3.8)
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, 3, [1, 2], [1, 3])
        with self.assertRaises(TypeError):
            r5 = Rectangle(2, 3, {'value': 2}, {'value': 3})
        with self.assertRaises(TypeError):
            r6 = Rectangle(2, 3, (1, 2), (1, 3))
        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 3, -2, -3)
        r8 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 0)
        r9 = Rectangle(2, 3, 234572815350000000000000, 125400000000000000000000)
        self.assertEqual(r9.y, 125400000000000000000000)
        self.assertEqual(r9.x, 234572815350000000000000)
