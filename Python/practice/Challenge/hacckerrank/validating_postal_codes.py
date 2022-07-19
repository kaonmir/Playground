#!/usr/bin/python3

"""
100,000 <= P <= 999,999
P not in alternating repetitive digit pair; "aba" structure
"""

regex_integer_in_range = r"^[1-9][0-9]{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.


import re

# P = input()
P = "0000"

a = re.findall(regex_alternating_repetitive_digit_pair, P)
print(a)
