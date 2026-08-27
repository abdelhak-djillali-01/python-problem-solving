#!/usr/bin/env python3

def word_count(sentence):
    return len(sentence.split())

print(word_count("the quick brown fox"))     # 4
print(word_count("  too   many   spaces  ")) # 3