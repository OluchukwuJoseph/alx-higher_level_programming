#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_string = ''
    for character in str:
        if i != n:
            new_string += str[i]
        i += 1
    return new_string
