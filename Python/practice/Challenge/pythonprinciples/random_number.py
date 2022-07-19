#!/usr/bin/python3


import random


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


previous_number = None


@print_decorator
def random_number():
    global previous_number

    random_number = 63 if previous_number == 42 else random.randint(0, 100)
    random_number = 1 if previous_number == 63 else random_number

    previous_number = random_number
    return random_number


for _ in range(100):
    random_number()
