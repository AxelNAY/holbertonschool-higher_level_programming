#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))

if number >= 1:
    number = 0
    for arg in argv:
        if number != 0:
            print("{}: {}".format(number, arg))
        number += 1

