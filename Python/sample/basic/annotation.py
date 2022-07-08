#!/usr/bin/python3


def add(a: int, b: int = 3) -> int:
    return a+b


if __name__ == "__main__":
    print(add(1, 2))
    print(add(1))
    print(add(1, 4, 5))
