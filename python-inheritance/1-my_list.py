#!/usr/bin/python3
"""mylist that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
