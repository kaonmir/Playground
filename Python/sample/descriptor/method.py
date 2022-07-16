#!/usr/bin/python3


from random import random


class K:
    classAttr = None

    def __init__(self):
        self.InstanceAttr = None

    @classmethod
    def classMethod(first):
        print(first)

    @staticmethod
    def staticMethod(first):
        print(first)

    def InstanceMethod(first):
        print(first)


def main():
    k = K()

    K.InstanceMethod("normalMethod")
    K.classMethod()
    K.staticMethod("classMethod")

    k.InstanceMethod()
    k.classMethod()
    k.staticMethod("classMethod")

    print(K.__dict__.keys())
    print(k.__dict__.keys())

    print(K.__name__)
    print(k.__class__.__name__)


if __name__ == "__main__":
    main()
