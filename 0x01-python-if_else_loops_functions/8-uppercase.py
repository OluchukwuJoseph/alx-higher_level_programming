#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        ascii_code = ord(letter)
        if (ascii_code >= 95 and ascii_code <= 123):
            ascii_code = ascii_code - 32
        print("{}".format(chr(ascii_code)), end="")
    print()
