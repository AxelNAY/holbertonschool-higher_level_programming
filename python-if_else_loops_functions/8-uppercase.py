#!/usr/bin/python3
def uppercase(s):
    for letter in s:
        print("{:letter}".format(ord(letter) - 32
                            if 97 <= ord(letter) <= 122 else ord(letter)), end="")
    print()
