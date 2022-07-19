#!/usr/bin/python3


def _capital_indexes(string):
    for i in range(len(string)):
        if string[i].isupper():
            yield i


def capital_indexes(string):
    return list(_capital_indexes(string))
