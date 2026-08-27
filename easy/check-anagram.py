#!/usr/bin/env python3

def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello",  "world"))    # False
print(is_anagram("Astronomer", "Moon starer"))  # False (spaces matter)