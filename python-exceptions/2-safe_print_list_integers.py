#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            nb_print += 1
        except (ValueError, TypeError):
            try:
                continue
            except IndexError:
                break
    print()
    return nb_print
