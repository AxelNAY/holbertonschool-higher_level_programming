#!/usr/bin/python3
"""Write an empty class """


class Rectangle:
    """Define a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """current width of the rectangle"""
        return self.__width

    @width.setter
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
        return self.__height

    @height.setter
    def height(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with #"""
        empty = ""
        result = []
        if self.__width == 0 or self.__height == 0:
            return empty
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """return a representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """print a sentence after deleting the rectangle"""
        print("Bye rectangle...")
