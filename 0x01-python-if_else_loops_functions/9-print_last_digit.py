#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    temp = number % 10
    print(temp, end="")
    return temp
