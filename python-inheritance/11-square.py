#!/usr/bin/python3
"""Write a class Square who inherit
from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Define a Square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): size of the square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the rectangle area"""
        return self.__size * self.__size

    def __str__(self):
        """print Rectangle with the width and height"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
