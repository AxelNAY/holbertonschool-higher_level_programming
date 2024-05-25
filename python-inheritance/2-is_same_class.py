#!/usr/bin/python3
"""returns True if the object is"""


def is_same_class(obj, a_class):
    """If the object is exactly an instance
    of the specified class return True ; otherwise False."""
    return type(obj) is a_class
