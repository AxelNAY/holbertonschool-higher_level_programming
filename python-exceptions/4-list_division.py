#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            result = 0
            try:
                result = my_list_1[idx] / my_list_2[idx]
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            finally:
                print("Inside result: {}".format(result))
                return result
        except (ValueError, TypeError):
            try:
                print("wrong type")
                continue
            except IndexError:
                print("out of range")
                break
        finally:
    print()
    return nb_print
