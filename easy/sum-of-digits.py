#!/usr/bin/env python3

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

print(sum_of_digits(123)) #6
print(sum_of_digits(-456)) #15