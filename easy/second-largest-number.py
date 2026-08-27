#!/usr/bin/env python3

def second_largest(numbers):
    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        raise ValueError("Need at least two distinct numbers")

    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)

print(second_largest([4, 1, 9, 9, 3]))
print(second_largest([10, 20, 30])) 