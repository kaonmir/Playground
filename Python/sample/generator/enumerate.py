#!/usr/bin/python3


def enum(input):
    for i in range(len(input)):
        yield i, input[i]


def main():
    for i, j in enumerate(["a", "b", "c"]):
        print(i, j)

    for i, j in enum(["a", "b", "c"]):
        print(i, j)


if __name__ == "__main__":
    main()
