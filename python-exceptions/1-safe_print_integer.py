#!/usr/bin/python3
def safe_print_integer(value):
    value += 0
    try:
        print("{}".format(value))
        return True
    except TypeError:
        return False
    return verif
