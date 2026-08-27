#!/usr/bin/env python3

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Racecar"))  # True
print(is_palindrome("hello"))    # False