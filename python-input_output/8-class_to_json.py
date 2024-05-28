#!/usr/bin/python3
"""Returns the dictionary description with simple data structure
for JSON serialization of an object"""

import json

def class_to_json(obj):
    desc = {}

    for item_name in dir(obj):
        if not item_name.startswith('__'):
            item_value = getattr(obj, item_name)
            if isinstance(item_value, (list, dict, str, int, bool)):
                desc = [item_name] = item_value

    return desc
