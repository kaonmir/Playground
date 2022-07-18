#!/usr/bin/python3


from operator import xor


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def list_xor(n, list1, list2):
    return xor(n in list1, n in list2)


list_xor(1, [1, 2, 3], [4, 5, 6])  # True
list_xor(1, [0, 2, 3], [1, 5, 6])  # True
list_xor(1, [1, 2, 3], [1, 5, 6])  # False
list_xor(1, [0, 0, 0], [4, 5, 6])  # False
