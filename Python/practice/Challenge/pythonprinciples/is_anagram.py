#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        string1 = string1.lower()
        string2 = string2.lower()
        for char in string1:
            if char in string2:
                string2 = string2.replace(char, "", 1)
            else:
                return False
        return True


is_anagram("typhoon", "opython")
is_anagram("Alice", "Bob")
