#!/usr/bin/python3
"""This module contains tests for Base class
   tests/test_base.py
"""
from models.base import Base
import unittest

class Test_Base(unittest.TestCase):
    def test_instance(self):
        """
            Test if Base actually creates an instance
        """
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_when_id_is_none(self):
        """
            Test when id is none
        """
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)

    def test_when_id_is_not_none(self):
        """
            test when id is not none
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base(20)
        self.assertEqual(b3.id, 20)
