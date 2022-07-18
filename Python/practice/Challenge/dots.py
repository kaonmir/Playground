#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def add_dots(string):
    # adds "." in between each letter
    string = string.replace("", ".", len(string))
    return string[1:]


def remove_dots(string):
    # removes "." in between each letter
    string = string.replace(".", "")
    return string
