#!/usr/bin/env python3

def reverse_list(lst):
    result = []

    for index in range(len(lst) - 1, -1, -1):
        result.append(lst[index])

    return result

print(reverse_list([1, 2, 3, 4, 5]))