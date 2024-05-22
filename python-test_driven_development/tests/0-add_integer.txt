``0-add_integer`` module test
=============================

Using ``add_integer`` function
-------------------------------

This text file contains test cases for the function ``add_integer``.
First import function to the varaible add_integer:
    
    >>> add_integer = __import__('0-add_integer').add_integer

Test for success
================

    >>> add_integer(2, 1)
    3

    >>> add_integer(100, -2)
    98

    >>> add_integer(-2, 100)
    98

    >>> add_integer(2)
    100

    >>> add_integer(100.3, -2)
    98

    >>> add_integer(-2.2, 100.3)
    98

================
Test for fail
================

    >>> add_integer("Holberton", 6)
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer("Holberton", "School")
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer()
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer(30, 35, 40)
    Traceback (most recent call last):
    TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

    >>> add_integer(100, None)
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer(45, [50, 60])
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer(float("nan"))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer

    >>> add_integer(float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer
