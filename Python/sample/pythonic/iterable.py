#!/usr/bin/python3


from contextlib import contextmanager
import contextlib


class CustomSequence:
    def __init__(self):
        self._range = [1, 2, 3, 4, 5]

    # __len__ method를 없애고 실행하면,
    # 아무것도 출력되지 않는다.
    def __len__(self):
        return 2

    # def __getitem__(self, index):
    #     return self._range[index]


def main():
    arr = [1, 2, 3]
    for i in range(5):
        print(arr[i])


if __name__ == "__main__":
    main()
