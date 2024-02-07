#!/usr/bin/python3
"""This module contains the append_write() function
   2-append_write.py
"""


def append_write(filename="", text=""):
    """
        Appends text to a text file and return the number of characters added

        Args:
            filename (str): The name of the text file to append to.
            text (str): The text to be added

        Returns:
            Number of character added
    """
    with open(filename, 'a') as file:
        length = file.write(text)
        return length
