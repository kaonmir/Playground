#!/usr/bin/python3


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_decorator
def validate(code):
    include_list = {
        "def": "missing def",
        ":": "missing :",
        "(": "missing paren",
        ")": "missing paren",
        "validate": "wrong name",
        "    ": "missing indent",
        "return": "missing return",
    }

    exclude_list = {
        "()": "missing param",
    }

    include_result = [l[1] for l in include_list.items() if l[0] not in code]
    if len(include_result) != 0:
        return include_result[0]

    exclude_result = [l[1] for l in exclude_list.items() if l[0] in code]
    if len(exclude_result) != 0:
        return exclude_result[0]

    return True


validate("def foo():\n print(123)")  # missing param
