#!/usr/bin/python3
import copy
def search_replace(my_list, search, replace):
    new_list = copy.deepcopy(my_list)
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
        elif my_list[i] == replace:
            my_list[i] = search
    return new_list
