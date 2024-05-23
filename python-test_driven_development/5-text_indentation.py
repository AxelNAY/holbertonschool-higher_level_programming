#!/usr/bin/python3
"""Contain a function that prints a text with 2 new lines after a symbol"""


def text_indentation(text):
    """prints a text with 2 new lines after one of these characters: ., ? or :
    
    Args:
    text (str): a long text with symbol.

    Raises:
    TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for letter in text:
        print("{}".format(letter), end="")
        if letter == "." or letter == "?" or letter == ":":
            print()
            print()
