#!/usr/bin/env python3

def c_to_f(c):
    return round(c * 1.8 + 32, 2)

def f_to_c(f):
    return round((f - 32) * 1.8, 2)

print(c_to_f(100))  # 212.0
print(f_to_c(32))   # 0.0
print(c_to_f(37))   # 98.6

