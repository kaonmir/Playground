#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
