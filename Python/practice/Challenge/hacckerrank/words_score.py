#!/usr/bin/python3

"""
For each word,
    even number of vowels : 2
    otherwise : 1
"""


def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u", "y"]


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


print(score_words(["hello"]))  # 2
print(score_words(["hello"]))  # 2
print(score_words(["hello", "world", "after", "all", "hello"]))  # 8
