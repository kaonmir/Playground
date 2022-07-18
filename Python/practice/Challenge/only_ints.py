#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def only_ints(number1, number2):
    if type(number1) is int and type(number2) is int:
        return True
    else:
        return False


only_ints(1, 2)
only_ints("a", 1)
only_ints(1, True)
