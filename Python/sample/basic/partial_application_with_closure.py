#!/usr/bin/python3

from functools import partial


def sum(a, b, c, d, e,   f):
    return a + b + c + d + e + f


def main():
    print("=== use sum function ===")
    part = partial(sum, 1, 2, 3, 4)
    print(part(5, 6))


if __name__ == "__main__":
    main()
