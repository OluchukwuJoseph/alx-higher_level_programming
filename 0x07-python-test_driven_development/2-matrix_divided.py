#!/usr/bin/python3
"""2-matrix_divided.py
This module contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix.
    Args:
        matrix (list of lists): the matrix to be divided.
        div (int or float): the divisor to divide the matrix.

    Return:
        new_matrix (list of lists): returns the new list created
        else raise an error.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        ZeroDivisionError: If `div` is zero.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check length of lists in matrix
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
        if len(matrix) - i > 1:
            if type(matrix[i + 1]) is not list:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
        if matrix[i] is not matrix[-1]:
            # compare length of each list in matrix
            if len(matrix[i]) == len(matrix[i + 1]):
                # check if items in list in matrix is an int or float
                for item in matrix[i]:
                    if not isinstance(item, (int, float)):
                        raise TypeError("matrix must be a matrix"
                                        " (list of lists) of integers/floats")
            else:
                raise TypeError("Each row of the matrix"
                                " must have the same size")
        # compare length of last list in matrix with previous list
        if matrix[i] is matrix[-1] and i != 0:
            if len(matrix[i]) == len(matrix[i - 1]):
                # check if items in last list in matrix is an int or float
                for item in matrix[i]:
                    if not isinstance(item, (int, float)):
                        raise TypeError("matrix must be a matrix"
                                        " (list of lists) of integers/floats")

    new_matrix = [[round(i / div, 2) for i in lists] for lists in matrix]
    return new_matrix
