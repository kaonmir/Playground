#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]


zap([0, 1, 2, 3], [5, 6, 7, 8])
