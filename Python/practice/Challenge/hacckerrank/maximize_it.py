#!/usr/bin/python3
"""
Given,
    function f(x)=x^2
    K lists where K[i] consists of N_i elements
max(sig(f(X_n)) % M),
    where 1 <= X_n <= k
    X_n is a element of the list K[i]

"""

from itertools import product


def sum_mod(l, M):
    answer = 0
    for x in l:
        answer += x
        answer %= M
    return answer


def maximize(lists, M):
    lists = [list(set(l)) for l in lists]
    pow_module = lambda x: pow(x, 2, M)
    lists = map(lambda l: map(pow_module, l), lists)
    return max(map(lambda x: sum_mod(x, M), product(*lists)))


def test():
    print(maximize([[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]], 1000))  # 206
    print(maximize([[2], [3], [5, 10]], 39))  # 38
    print(maximize([[1, 2], [3, 4], [5, 10]], 3))  # 2
    print(maximize([[1, 1], [1], [1, 2, 1], [1, 1]], 7))  # 4


def main(validate=None):
    if validate is None:
        k, M = input().split()
        lists = [map(int, input().split()[1:]) for _ in range(int(k))]
        print(maximize(lists, int(M)))
    else:
        test()


main("test")
