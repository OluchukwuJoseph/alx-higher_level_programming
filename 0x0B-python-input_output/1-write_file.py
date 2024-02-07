#!/usr/bin/python3
"""This module contains the function write_file()
1-write_file.py
"""


def write_file(filename="", text=""):
    """
        Writes to a text file and return the number of characters written

        Args:
            filename (str): The name of the text file to write to.
            text (str): The text to be written in file

        Returns:
            None
    """
    with open(filename, 'w') as file:
        length = file.write(text)
        return length
