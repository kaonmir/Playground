#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def count(string):
    return len(string.split("-"))


count("ho-tel")
count("cat")
count("met-a-phor")
count("ter-min-a-tor")
