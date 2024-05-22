#!/usr/bin/python3
"""This module contain a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided function divides all elements of a matrix

    Args:
    matrix (list of lists): two dimension matrix
    div (int, float): divisor

    Returns:
        list of lists: all elements divided inside a new matrix"""

    if type(matrix) != list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # capture the first row len
    len_row = len(matrix[0])

    # validate div conditions
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # validate rows len in matrix and values inside each list
    for idx in matrix:
        if type(idx) != list or idx == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(idx) == len_row:
            for j in idx:
                if type(j) != int and type(j) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            raise TypeError("Each row of the matrix must have the same size")

    return list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))
