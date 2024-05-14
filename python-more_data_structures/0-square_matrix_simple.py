#!/usr/bin/python3
import copy
def square_matrix_simple(matrix=[]):
    new_matrix = copy.deepcopy(matrix)
    for row in new_matrix:
        for i in range(len(row)):
            row[i] = row[i] * row[i]
    return new_matrix
