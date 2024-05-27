#!/usr/bin/python3
"""Creates an Object from a JSON file"""

import json

def load_from_json_file(filename):
    """Creates an Object from a JSON fil

    Args:
        filename: name of the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.loads(my_obj))
