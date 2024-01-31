#!/usr/bin/python3
"""
101-locked_class.py
This Module contains a class called LockedClass
"""


class LockedClass:
    """
    This class only allows one instance attribute
    """
    __slots__ = ('first_name')
