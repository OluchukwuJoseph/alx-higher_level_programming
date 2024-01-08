#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for x in item:
            if x == item[-1]:
                print("{:d}".format(x), end="")
            else:
                print("{:d} ".format(x), end="")
        print()
