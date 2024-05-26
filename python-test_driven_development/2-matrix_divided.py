#!/usr/bin/python3
"""This module contain a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided function divides all elements of a matrix

    Args:
    matrix (list of lists): two dimension matrix
    div (int, float): divisor

    Returns:
        list of lists: all elements divided inside a new matrix
    
    Raises:
    TypeError: If the matrix is not a list of integer or float
    of integers or floats,
               or if each row of the matrix does not have the same size,
               or if the divisor is not a number.
    ZeroDivisionError: If the divisor is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(error)
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(error)

    len_row = len(matrix[0])
    if not all(len(row) == len_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2)
        for elem in row] for row in matrix]
    return new_matrix
