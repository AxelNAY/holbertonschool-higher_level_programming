#!/usr/bin/python3
"""Serialization and deserialization using XML
as an alternative format to JSON."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary in a XML file.

    Args:
        dictionary (dict): a Python dictionary.
        filename (str): name of the XML file."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize a XML file into a Python dictionary.
    
    Args:
        dictionary: A Python dictionary

    Return:
        A Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
