#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix
by a number and rounds to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): list of lists of integers or floats
        div (int or float): number to divide matrix by
    Returns:
        list: new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
