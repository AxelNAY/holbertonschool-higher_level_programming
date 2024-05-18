#!/usr/bin/python3
"""Write an empty class """


class Square:
    """Define a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
        size: size
        position: position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """value is the square length"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print a square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
