#!/usr/bin/env python3

def find_max(lst): 
    if not lst:
        raise ValueError("List is empty")

    largest = lst[0]
    for n in lst[1:]:
        if n > largest:
            largest = n

    return largest

print(find_max([3, 1, 9, 2, 7]))  # 9