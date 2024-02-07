#!/usr/bin/python3
"""This module contains the function pascal_triangle()
    12-pascal_triangle.py
"""


def pascal_triangle(n):
    """Creates a matrix of integers that represents Pascal’s triangle of n

        Parameter:
            n (int): Number of list the matrix should have

        Return:
            Matrix
    """
    matrix = []
    if n <= 0:
        return matrix

    for i in range(n):
        my_list = []
        # fill up list with 1's
        while len(my_list) < (i + 1):
            my_list.append(1)

        if i < 2:
            matrix.append(my_list)
            continue

        k = 0
        j = 0
        for j in range(len(my_list)):
            # check if j (index) is referencing to the first or last index
            if j != (len(my_list) - 1) and j != 0:
                # checks if k is not more than the elements we are able to
                # reference to avoid IndexError
                if k < len(matrix[i - 1]) - 1:
                    my_list[j] = matrix[i - 1][k] + matrix[i - 1][k + 1]
                    k += 1

        matrix.append(my_list)

    return matrix
