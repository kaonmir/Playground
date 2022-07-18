#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def double_letters(string):
    for i, char in enumerate(string):
        if i + 1 < len(string) and char == string[i + 1]:
            return True
    return False


double_letters("hello")  # True
double_letters("nono")  # False
