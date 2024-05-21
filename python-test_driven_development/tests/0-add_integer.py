``0-add_integer`` module test
=============================

Using ``add_integer`` function
-------------------------------

This text file contains test cases for the function ``add_integer``.
First import function to the varaible add_integer:
    
    >>> add_integer = __import__('0-add_integer').add_integer

Test for success
================

Test_1 adding two integers
----------------------
    >>> add_integer(2, 1)
    3

Test_2 adding two integer with b being a negative value
-------------------------------------------------------------
    >>> add_integer(100, -2)
    98

Test_3 passing only one argument with b initiate to 98
--------------------------
    >>> add_integer(2)
    100

Test_4 adding a float with a negative integer
--------------------------
    >>> add_integer(100.3, -2)
    98

================
Test for fail
================

Test_5 adding an integer with a string
--------------------------
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer

Test_6 adding just first parameter as None
------------------------------------------
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
