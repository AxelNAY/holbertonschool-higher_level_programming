#!/usr/bin/python3
"""Write an empty class """


class Rectangle:
    """Define a Rectangle."""
    
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """current width of the rectangle"""
        return (self.__width)

    @property.setter
    def width(self, value):
        """value is the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """current height of the rectangle"""
        return (self.__height)

    @property.setter
    def width(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
