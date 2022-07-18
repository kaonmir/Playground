#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def online_count(dictionary):
    return len([1 for key in dictionary if dictionary[key] == "online"])


online_count({"a": "online", "b": "offline", "c": "online"})  # 2
online_count({"a": "online", "b": "offline", "c": "online", "d": "offline"})  # 2
online_count(
    {"a": "online", "b": "offline", "c": "online", "d": "offline", "e": "online"}
)  # 3
