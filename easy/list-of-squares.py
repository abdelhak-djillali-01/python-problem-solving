#!/usr/bin/env python3

def squares(n):
    return [x ** 2 for x in range(1, n + 1)]

print(squares(10)) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]