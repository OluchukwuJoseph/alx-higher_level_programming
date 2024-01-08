#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        try:
            a = tuple_a[i]
        except IndexError:
            a = 0
        try:
            b = tuple_b[i]
        except IndexError:
            b = 0
        new_tuple += (a + b, )
    return new_tuple
