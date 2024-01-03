#!/usr/bin/python
def print_last_digit(number):
    temp = number
    temp = str(temp)
    temp = temp[-1]
    print(temp, end="")
    return temp
