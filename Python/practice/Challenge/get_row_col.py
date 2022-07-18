#!/usr/bin/python3


import re

from requests import get


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def get_row_col(string):
    return (int(string[1]) - 1, ord(string[0]) - ord("A"))


get_row_col("A1")  # (0,0)
get_row_col("A2")  # (1,0)
get_row_col("A3")  # (2,0)

get_row_col("B2")  # (1,1)
