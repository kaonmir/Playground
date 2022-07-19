#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def all_equal(nums):
    return len([n for n in nums if n != nums[0]]) == 0


all_equal([1, 1, 1])
