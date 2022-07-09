#!/usr/bin/python3


from json.encoder import INFINITY
from operator import xor


def add(a):
    return a + 2


def main():
    k = [(1, 2), (2, 3)]

    print(list(map(add, [1, 2, 3])))


if __name__ == "__main__":
    main()
