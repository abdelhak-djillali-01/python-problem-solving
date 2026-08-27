#!/usr/bin/env python3

def flatten(matrix):
    return [item for row in matrix for item in row]

matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(flatten(matrix))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]