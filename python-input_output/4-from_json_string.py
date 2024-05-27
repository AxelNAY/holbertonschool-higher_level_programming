#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string"""

import json

def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_obj: an object

    Return:
        A JSON representation of the object"""
    return json.loads(my_str)
