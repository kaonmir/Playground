#!/usr/bin/python3


class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    # def __getattr__(self, attr):
    #     print(attr + " attribute is not defined")


def main():
    attr = DynamicAttributes("abc")
    # print(attr.__getattribute__("attributes"))
    print(dir(attr.asd))
    pass


if __name__ == "__main__":
    main()
