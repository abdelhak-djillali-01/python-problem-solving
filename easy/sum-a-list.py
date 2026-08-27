#!/usr/bin/env python3

from functools import reduce

def list_sum(lst):
    return reduce(lambda a, b: a + b, lst, 0)

print(list_sum([1, 2, 3, 4, 5]))    # 15
print(list_sum([10, -3, 7, 2.5]))   # 16.5