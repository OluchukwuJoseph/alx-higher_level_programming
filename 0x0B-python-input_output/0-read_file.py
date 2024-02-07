#!/usr/bin/python3
"""This module contains the read_file function
    0-read_file.py
"""


def read_file(filename=""):
    """
        Reads a text file and prints its content to the standard output.

        Args:
            filename (str): The name of the text file to read.

        Returns:
            None
    """
    with open(filename) as file:
        print(file.read(), end="")
