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

    i = 0
    while i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
            i += 1
            if i < len(text) and text[i + 1] == " ":
                i += 1
            continue
        i += 1
