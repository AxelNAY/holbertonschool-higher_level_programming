#!/usr/bin/python3
"""Returns the dictionary description with simple data structure
for JSON serialization of an object"""

import json

def class_to_json(obj):
    """Convert the dictionary description in JSON
    Return:
        The dictionary description in JSON"""
    return obj.__dict__
