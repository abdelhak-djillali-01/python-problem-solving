#!/usr/bin/env python3

def times_table(n):
    for i in range(1, 13):
        print(f"{i} x {n} = {i * n}")

times_table(5)