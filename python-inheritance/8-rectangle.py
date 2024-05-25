#!/usr/bin/python3
"""Write a class Rectangle who inherit
from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Define a Rectangle."""

    def __init__(self, width, height):
        """Initialize a new rectangle.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
