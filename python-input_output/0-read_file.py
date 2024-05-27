#!/usr/bin/python3
"""Print the contain of the file my_file_0.txt"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout
    Arg:
        filename: name of the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
