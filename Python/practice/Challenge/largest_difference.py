#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def largest_difference(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None

    max_value = max(list_of_numbers)
    min_value = min(list_of_numbers)
    return max_value - min_value
