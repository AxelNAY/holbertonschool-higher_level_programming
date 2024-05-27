#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)
and returns the number of characters"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters
    Args:
        filename: name of the file
        text: text to put in the file

    Return:
        The number of characters put in the file"""
    with open(filename, 'a', encoding="utf-8") as f:
        nb_characters = f.write(text)

    return nb_characters
