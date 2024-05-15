#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    replace = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        replace = {key: new_value}
        new_dict.update(replace)
    return new_dict
