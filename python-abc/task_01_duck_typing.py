#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the form area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the form perimeter"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area area"""
        return abs(math.pi * self.radius ** 2)

    def perimeter(self):
        """Return the circle perimeter"""
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and the perimeter of the form"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
