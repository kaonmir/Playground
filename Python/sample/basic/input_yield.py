#!/usr/bin/python3

def gen():
    while True:
        value = yield
        yield value


def main():
    print("=== print gen function ===")
    g = gen()

    next(g)
    a = g.send(3)
    next(g)
    b = g.send(5)
    next(g)

    print(a, b)


if __name__ == "__main__":
    main()
