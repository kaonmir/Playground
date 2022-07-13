#!/usr/bin/python3


from pyrsistent import b


class MyClass:
    def __init__(self):
        print("MyClass.__init__() called")

    def __call__(self):
        print("MyClass.__call__() called")


def myFunction():
    print("myFunction() called")


def main():
    a = MyClass()
    a()

    myFunction()
    pass


if __name__ == "__main__":
    main()
