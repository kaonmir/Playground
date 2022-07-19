#!/usr/bin/python3


def is_leap(year):
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False


print(is_leap(1990))  # False
