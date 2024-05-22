#!/usr/bin/python3
"""Contains a function who print My name is <first name> <last name>
args: first name and last name must be a string
return: print first name and last name"""


def say_my_name(first_name, last_name=""):
    """function that print the first name and the last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
