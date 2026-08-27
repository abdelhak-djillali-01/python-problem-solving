#!/usr/bin/env python3

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1