#!/usr/bin/python3
"""Basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and
deserialize the JSON file to recreate the Python Dictionary."""


import json

def serialize_and_save_to_file(data, filename):
    """Serialize the data and save into a file.

    Args:
        data (dict): A Python Dictionary with data.
        filename (str): The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize the JSON file to recreate the Python Dictionary.

    Args:
        filename (str): The name of the file.

    Returns:
        A Python Dictionary with the deseialized JSON data from the file."""
    with open(filename, 'r') as file:
        return json.load(file)
