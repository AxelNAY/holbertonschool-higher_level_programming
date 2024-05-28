#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then save them to a file"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_set = load_from_json_file(filename)
except FileNotFoundError:
    my_set = []

my_set.extend(sys.argv[1:])

save_to_json_file(my_set, filename)
