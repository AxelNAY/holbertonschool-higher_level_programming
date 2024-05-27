#!/usr/bin/python3
"""Print the contain of the file my_file_0.txt"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written
    Args:
        filename: name of the file
        text: text to put in the file

    Return:
        The number of characters put in the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        nb_characters = f.write(text)

    return nb_characters
