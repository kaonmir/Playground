#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def mid(string):
    return string[len(string) // 2] if len(string) % 2 != 0 else ""


mid("abc")  # b
mid("abcd")  # ""
