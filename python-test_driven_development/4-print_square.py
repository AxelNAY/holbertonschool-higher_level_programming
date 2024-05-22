#!/usr/bin/python3
"""Print a square"""


def print_square(size):
    """Print a square with the symbol #
    Parametres:
    size (int): size of a square

    Raise:
    TypeError: size must be an integer
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
