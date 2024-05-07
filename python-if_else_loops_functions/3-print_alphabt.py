#!/usr/bin/python3
letter = 97
while letter < 123:
    if chr(letter) not in 'qe':
        print(f"{chr(letter)}", end="")
    letter += 1
