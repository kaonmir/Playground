#!/usr/bin/python3
"""
alphanumeric, space, !,@,#,$,%,&

if aba where a is alphanumeric and b is not, then replcae b with ''

"""


from itertools import chain
import re


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
template = f"%{m}s"

for _ in range(n):
    matrix_item = template % (input())
    matrix.append(matrix_item)


def transpose(matrix):
    return list(zip(*matrix))


def matrix_script(matrix):
    sentence: str = "".join(chain(*transpose(matrix)))
    return re.sub(r"(?<=[0-9A-Za-z])[^0-9A-Za-z]+(?=[0-9A-Za-z])", " ", sentence)


print(matrix_script(matrix))
