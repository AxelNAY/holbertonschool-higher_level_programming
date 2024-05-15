#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    numb = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            if i != len(roman_string) - 1 and roman_string[i + 1] != "V" or roman_string[i + 1] != "X":
                numb += 1
        elif roman_string[i] == "V":
            numb += 5
        elif roman_string[i] == "X":
            if i != len(roman_string) - 1 and roman_string[i + 1] != "L" or roman_string[i + 1] != "C":
                numb += 10
        elif roman_string[i] == "L":
            numb += 50
        elif roman_string[i] == "C":
            if i != len(roman_string) - 1 and roman_string[i + 1] != "D" or roman_string[i + 1] != "M":
                numb += 100
        elif roman_string[i] == "D":
            numb += 500
        elif roman_string[i] == "M":
            numb += 1000
    return numb
