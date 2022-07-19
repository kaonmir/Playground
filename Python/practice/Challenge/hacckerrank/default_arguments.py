#!/usr/bin/python3
"""
To debug the code to make it execute

Debug the given function print_from_stream using the default value of one of its arguments
The function should print n values in a separate line returned by the get_next() method of the stream object.
Whenever the function is called without a stream object, the EvenStream object will be used.
"""


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())

print_from_stream(10, OddStream())  # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
print_from_stream(5, OddStream())  # 1, 3, 5, 7, 9
