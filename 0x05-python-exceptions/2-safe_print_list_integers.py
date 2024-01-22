#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    amount_of_integers = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            amount_of_integers += 1
        except Exception as error:
            if isinstance(error, TypeError):
                continue
            elif isinstance(error, ValueError):
                continue
            elif isinstance(error, IndexError):
                raise IndexError("list index out of range")
                return amount_of_integers
    print()
    return amount_of_integers
