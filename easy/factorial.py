#!/usr/bin/env python3

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers have no factorial")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(0))  # 1
print(factorial(5))  # 120
print(factorial(7))  # 5040