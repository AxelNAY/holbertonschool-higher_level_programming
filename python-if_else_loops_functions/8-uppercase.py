#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        result += letter
    print('{}'.format(result))
