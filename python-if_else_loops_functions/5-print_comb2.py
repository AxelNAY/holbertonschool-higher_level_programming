#!/usr/bin/python3
dec = 0
last_digit = 0
while dec < 10 or last_digit < 10:
    last_digit = 0
    while last_digit < 10:
        if dec != 9 or last_digit != 9:
            print(f"{dec}{last_digit}", end=", ")
        else:
            print(f"{dec}{last_digit}")
        last_digit += 1
    dec += 1
