#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def consecutive_zeros(string):
    return max(map(lambda l: len(l), string.split("1")))


consecutive_zeros("1001101000110")
