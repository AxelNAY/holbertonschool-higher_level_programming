#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    numb1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    numb2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    numb3 = tuple_b[0] if len(tuple_b) >= 1 else 0
    numb4 = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (numb1 + numb3, numb2 + numb4)
