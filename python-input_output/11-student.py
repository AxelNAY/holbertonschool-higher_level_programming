#!/usr/bin/python3
"""A class Student that returns the dictionary description
with simple data structure for JSON serialization of an object"""


class Student:
    """Class representing a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new square.

        Args:
            first_name (string): first name of the student
            last_name (string): last name of the student
            age (int): age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the dictionary description in JSON
        Return:
            The dictionary description in JSON"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for idx in attrs:
                if idx in self.__dict__:
                    new_dict[idx] = self.__dict__[idx]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): a dictionnary contening the Student attributes"""
        for idx in json:
            self.__dict__[idx] = json[idx]
