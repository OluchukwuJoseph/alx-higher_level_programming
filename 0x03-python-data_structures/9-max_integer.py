#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for number in my_list:
        if my_list[0] == number:
            max_number = number
        if max_number < number:
            max_number = number
    return max_number
