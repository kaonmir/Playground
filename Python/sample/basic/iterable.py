#!/usr/bin/python3

def main():
    x = [1, 2, 3]

    x_iterator = iter(x)

    print("%s" % x_iterator)
    print("iterator next : %s" % next(x_iterator))
    print("iterator next : %s" % next(x_iterator))
    print("iterator next : %s" % next(x_iterator))


if __name__ == "__main__":
    main()
