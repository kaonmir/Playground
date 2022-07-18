#!/usr/bin/python3


from operator import xor


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def param_count(*args):
    return len(args)


param_count()  # 0
param_count(2, 3, 4)  # 3
